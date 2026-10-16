# Restart automático periódico — loop de renovação de cota (`maxEvents`/`fork.maxForks`)

> **Purpose**: Documentar o loop de restart automático (`scripts/shadowtraffic/shadowtraffic-restart-loop.ps1`) que renova periodicamente a cota vitalícia dos generators do `gen-unified`, sempre via caminho seguro (`toggle-shadowtraffic.ps1`), sem reimplementar o recálculo de `startingFrom`.
> **Confidence**: 0.95 — arquitetura de auto-preservação validada de forma independente por agente `the-planner` e testada contra infraestrutura Docker real (`-IntervalSeconds 15`), ciclo completo + `off` externo confirmados em log (sessão 2026-09-29, ver `.claude/dev/tasks/PROMPT_SHADOWTRAFFIC_RESTART_LOOP.md`).

## When to Use

- Ao decidir como manter o `gen-unified` gerando eventos por um período longo (horas/dias) sem intervenção manual.
- Ao investigar por que um generator "parou de gerar eventos sozinho" mesmo sem erro — pode ser um teto vitalício (`maxEvents`/`maxForks`) atingido, e o fix é restart (via loop ou manual), nunca alterar o config para "consertar".
- Antes de subir/derrubar `gen-unified` manualmente enquanto o loop de restart estiver ativo — usar sempre `toggle-shadowtraffic.ps1`, nunca `docker-compose`/`docker restart` diretos, mesmo com o loop rodando.
- Ao editar `toggle-shadowtraffic.ps1` ou `shadowtraffic-restart-loop.ps1` — entender a dependência de PID (`&` vs. `Start-Process`) antes de mexer, ver seção "Arquitetura de auto-preservação".

## O problema: teto vitalício por processo

Os generators do `shared/gen/unified/uber-eats.json.template` têm limites que valem para a vida do **processo Java**, não do banco:

- `localConfigs.maxEvents` — afeta `restaurants`, `products`, `inventory`, `users`.
- `fork.maxForks` + `keepAlive: true` — afeta `orders`, `payments`, `order_items`.

Ao atingir o teto, aquele generator para de emitir eventos **para sempre** dentro daquele processo — não há como "resetar a contagem" sem reiniciar o container. Sem intervenção, o pipeline degrada silenciosamente: generators vão parando um a um até sobrar pouco ou nenhum tráfego novo, sem nenhum erro nos logs.

Reiniciar "cru" (`docker-compose restart`/`stop`+`start` direto) **não resolve com segurança** — colide PK porque `startingFrom` é um valor fixo dentro do `uber-eats.json` gerado. Esse é exatamente o incidente documentado em [`restart-seguro-startingFrom.md`](restart-seguro-startingFrom.md) (17 streams travados, CPU 99%, zero linhas novas). O único caminho seguro é `scripts/shadowtraffic/toggle-shadowtraffic.ps1`, cuja ação `on` roda `Sync-StartingPoints` (recalcula `startingFrom` a partir de `MAX(id)` real via `shared/gen/setup-configs.ps1` + queries Postgres/Oracle) antes de religar o container.

## A solução: loop que automatiza o caminho já seguro

`scripts/shadowtraffic/shadowtraffic-restart-loop.ps1` **não reimplementa nenhuma lógica de recálculo de PK** — ele só chama `toggle-shadowtraffic.ps1 -Action off` seguido de `-Action on` em um intervalo periódico, delegando 100% da segurança do restart ao script já existente.

```text
param([int]$IntervalSeconds = 7200)   # 2h padrão, sobrescrevível

loop:
  1. Test-ContainerRunning -Name "gen-unified"
     -> se NÃO ativo: loga e encerra (auto-término, mesmo padrão do
        shadowtraffic-report-loop.ps1 já existente para o loop de report)
  2. Start-Sleep -Seconds $IntervalSeconds
  3. checa container de novo; se ainda ativo, dispara o ciclo:
       Invoke-ToggleAction("off")   # sempre tentado
       Invoke-ToggleAction("on")    # SEMPRE tentado, mesmo se off falhar
                                     # (idempotente: cai no ramo "já ativo"
                                     #  se o container ainda estiver de pé)
  4. volta ao passo 1
```

`Invoke-ToggleAction` chama `& $togglePath -Action <off|on>` dentro de um `try/catch`, resetando e checando `$LASTEXITCODE` manualmente — necessário porque `toggle-shadowtraffic.ps1` usa `exit 1` em alguns caminhos de erro, e via `&` isso **não lança exceção**, só define `$LASTEXITCODE` e retorna silenciosamente. Cada resultado de ciclo (sucesso/aviso/erro) é logado em `logs/shadowtraffic-restart.log`.

## Arquitetura de auto-preservação (o ponto mais importante)

O loop chama `toggle-shadowtraffic.ps1` via operador **`&`** — nunca `Start-Process`. Em PowerShell, `&` executa o script-alvo no **mesmo processo/`$PID`** do chamador. É essa escolha que permite o loop sobreviver ao próprio ciclo de restart que ele mesmo dispara:

1. `Start-RestartLoop` spawna o loop via `Start-Process pwsh` (processo próprio, PID X) e grava esse PID em `logs/restart-loop.pid`.
2. Quando o intervalo vence, o loop (ainda rodando como PID X) executa `& $togglePath -Action off` **dentro de si mesmo** — não cria processo novo.
3. Dentro de `toggle-shadowtraffic.ps1`, ação `off`, a função `Stop-RestartLoop` lê `restart-loop.pid`, encontra o PID X — que é o próprio processo em execução (`[int]$procId -eq $PID`).
4. Quando os PIDs batem, `Stop-RestartLoop` **não mata o processo** (pula `Stop-Process`) — só loga em `logs/shadowtraffic-restart.log` que o loop sobrevive ao ciclo, e mantém `restart-loop.pid` intacto.
5. O mesmo processo então executa `& $togglePath -Action on`. Dentro de `on`, `Start-RestartLoop` chama `Test-RestartLoopRunning` — o PID em `restart-loop.pid` (ainda o próprio PID X) está vivo, então **não spawna um novo processo**.

Se `off` for chamado por **outro** processo (ex.: usuário rodando `toggle-shadowtraffic.ps1 -Action off` manualmente em outro terminal), o PID lido do arquivo não bate com o `$PID` desse chamador, e `Stop-RestartLoop` mata o loop normalmente — esse é o comportamento correto de desligamento externo, sem processo órfão nem PID duplicado.

### Funções novas em `toggle-shadowtraffic.ps1`

Paralelas às já existentes `Test-ReportLoopRunning`/`Start-ReportLoop`/`Stop-ReportLoop` (loop de report horário):

| Função | Papel |
|---|---|
| `Test-RestartLoopRunning` | Lê `restart-loop.pid`; valida também via `Get-CimInstance Win32_Process` que o `CommandLine` do PID vivo contém `shadowtraffic-restart-loop` — evita falso positivo por reaproveitamento de PID pelo Windows. |
| `Start-RestartLoop` | Spawna via `Start-Process pwsh` (não `powershell` 5.1 — `Sync-StartingPoints` usa `ConvertFrom-Json -Depth 100`, parâmetro só disponível a partir do PowerShell 6.2+/pwsh 7). Grava o PID em `logs/restart-loop.pid`. Chamada nos dois pontos onde `Start-ReportLoop` já era chamada (ramo "já ativo" e ramo de subida normal da ação `on`). |
| `Stop-RestartLoop` | Lógica de auto-preservação descrita acima. Chamada pela ação `off`. |

`toggle-shadowtraffic.ps1 status` ganhou uma linha adicional: "Loop de restart: ATIVO/PARADO".

## Logs e PID

| Arquivo | Conteúdo | Paralelo (loop de report) |
|---|---|---|
| `logs/shadowtraffic-restart.log` | Log de cada ciclo (sucesso/aviso/erro) | `logs/shadowtraffic-report.log` |
| `logs/restart-loop.pid` | PID do processo do loop de restart | `logs/report.pid` |

## Relação com `restart-seguro-startingFrom.md`

O restart automático só é seguro **porque** passa por `toggle-shadowtraffic.ps1`, que já resolve o `startingFrom` antes de religar (via `Sync-StartingPoints`). O loop de restart não reimplementa nenhuma lógica de recálculo de PK — apenas automatiza a chamada do caminho já seguro em um intervalo periódico. Qualquer alteração futura na lógica de `startingFrom` deve continuar vivendo só em `toggle-shadowtraffic.ps1`; o loop nunca deve ganhar lógica própria de cálculo de PK.

## Anti-Patterns

| Anti-Pattern | Por que é ruim | Fazer em vez disso |
|---|---|---|
| Chamar `toggle-shadowtraffic.ps1` via `Start-Process` dentro do loop | Quebra a auto-preservação — `Stop-RestartLoop` não reconheceria o PID do loop como "processo atual" e mataria o próprio loop a cada ciclo | Manter `&` (mesmo processo) |
| Rodar `docker restart gen-unified` manualmente enquanto o loop está ativo | Restart cru fora do `toggle-shadowtraffic.ps1` colide PK (ver `restart-seguro-startingFrom.md`) — o loop não protege contra restarts feitos por fora dele | Usar sempre `toggle-shadowtraffic.ps1` para qualquer restart manual, mesmo com o loop rodando |
| Assumir que `off` chamado de outro terminal também preserva o loop | Só preserva quando o PID do chamador é o mesmo do processo do loop (ciclo autodisparado); `off` externo mata o loop de propósito | Se quiser manter o loop vivo, não chamar `off` manualmente — deixar o próprio ciclo do loop religar |
| Usar `powershell` 5.1 para spawnar o loop | `Sync-StartingPoints` usa `-Depth 100` em `ConvertFrom-Json`, indisponível no PowerShell 5.1 | `Start-RestartLoop` já usa `Start-Process pwsh` — não alterar para `powershell.exe` |

## See Also

- [restart-seguro-startingFrom](restart-seguro-startingFrom.md) — por que restart cru colide PK e o que `toggle-shadowtraffic.ps1 on` faz para evitar isso
- [mutacao-real-fork-statemachine](../concepts/mutacao-real-fork-statemachine.md) — semântica de `fork`/`maxForks`/`keepAlive` (o teto que o loop existe para renovar)
- `scripts/shadowtraffic/toggle-shadowtraffic.ps1` — implementação do restart seguro e das funções `Test-RestartLoopRunning`/`Start-RestartLoop`/`Stop-RestartLoop`
- `scripts/shadowtraffic/shadowtraffic-restart-loop.ps1` — implementação do loop periódico
- `.claude/dev/tasks/PROMPT_SHADOWTRAFFIC_RESTART_LOOP.md` — Notes com a validação independente da arquitetura de auto-preservação (agente `the-planner`) e o teste contra infraestrutura real
