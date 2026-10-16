# ==============================================================================
# Script: shadowtraffic-restart-loop.ps1
# Descricao: Loop de background que reinicia o gerador gen-unified a cada 2h
#            (intervalo configuravel) exclusivamente via
#            toggle-shadowtraffic.ps1 off -> on, para liberar novos tetos
#            vitalicios de localConfigs.maxEvents / fork.maxForks+keepAlive
#            sem colidir PK -- o "on" recalcula "startingFrom" a partir do
#            MAX(id) real antes de religar (ver
#            .claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md).
#            Nunca chama o orquestrador de containers diretamente -- toda
#            interacao com o container passa por toggle-shadowtraffic.ps1.
#
#            Sobrevive ao proprio ciclo que ele dispara: chama
#            toggle-shadowtraffic.ps1 via operador '&' (nunca via cmdlet de
#            spawn de processo novo), o que mantem a execucao no MESMO
#            processo/$PID do loop --
#            Stop-RestartLoop (dentro do "off") reconhece esse PID como o
#            proprio loop (comparacao $PID -eq $procId lendo
#            logs/restart-loop.pid) e nao o mata, so registra que o loop
#            sobrevive ao ciclo. Se "off" for chamado por outro processo
#            (terminal externo), o PID nao bate e o loop e encerrado
#            normalmente -- comportamento correto (usuario pediu para
#            desligar tudo). Ver .claude/kb/shadowtraffic/patterns/
#            restart-automatico-periodico.md para o detalhamento completo.
#
#            Nao chamar diretamente -- iniciado e encerrado automaticamente
#            por toggle-shadowtraffic.ps1 (on/off) via Start-RestartLoop /
#            Stop-RestartLoop.
#
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

param(
    [int]$IntervalSeconds = 7200
)

$ErrorActionPreference = "Stop"

. "$PSScriptRoot\..\lib\shadowtraffic-common.ps1"

$repoRoot   = Get-RepoRoot
$logDir     = "$repoRoot\logs"
$logFile    = "$logDir\shadowtraffic-restart.log"
$togglePath = "$PSScriptRoot\toggle-shadowtraffic.ps1"

if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Executa uma acao do toggle (off/on) dentro do PROPRIO processo via '&' --
# nunca via cmdlet de spawn de processo novo (quebraria a auto-preservacao
# via comparacao de $PID, ver toggle-shadowtraffic.ps1::Stop-RestartLoop).
# $LASTEXITCODE e zerado
# antes de cada chamada porque toggle-shadowtraffic.ps1 usa "exit 1" em
# alguns caminhos de erro -- invocado via '&' isso NAO lanca excecao, apenas
# define $LASTEXITCODE e retorna silenciosamente, entao precisa ser checado
# manualmente (achado da validacao de arquitetura, ver Notes do PROMPT
# PROMPT_SHADOWTRAFFIC_RESTART_LOOP.md).
function Invoke-ToggleAction {
    param([Parameter(Mandatory = $true)][string]$Action)

    $global:LASTEXITCODE = 0
    try {
        & $togglePath -Action $Action
        if ($LASTEXITCODE -ne 0) {
            throw "toggle-shadowtraffic.ps1 -Action $Action saiu com codigo $LASTEXITCODE"
        }
        return $true
    } catch {
        Add-Content -Path $logFile -Value "  [ERRO] Falha em '$Action': $($_.Exception.Message)"
        return $false
    }
}

Add-Content -Path $logFile -Value "---- loop de restart iniciado (PID $PID), intervalo ${IntervalSeconds}s ----"

while ($true) {
    if (-not (Test-ContainerRunning -Name "gen-unified")) {
        Add-Content -Path $logFile -Value "---- gen-unified nao esta mais ativo, encerrando loop de restart ----`n"
        break
    }

    Start-Sleep -Seconds $IntervalSeconds

    # gen-unified pode ter sido desligado manualmente durante a espera --
    # checar de novo antes de disparar o ciclo.
    if (-not (Test-ContainerRunning -Name "gen-unified")) {
        Add-Content -Path $logFile -Value "---- gen-unified nao esta mais ativo (checado apos espera), encerrando loop de restart ----`n"
        break
    }

    $now = Get-Date
    Add-Content -Path $logFile -Value "==== $($now.ToString('yyyy-MM-dd HH:mm:ss')) - iniciando ciclo de restart (off + on) ===="

    $offOk = Invoke-ToggleAction -Action "off"

    # O "on" e SEMPRE tentado, mesmo se o "off" falhar: e idempotente (cai no
    # ramo "ja esta ativo" se o container ainda estiver de pe), e deixar o
    # gerador desligado por causa de uma falha transitoria no "off" seria
    # pior do que tentar religa-lo.
    $onOk = Invoke-ToggleAction -Action "on"

    if ($offOk -and $onOk) {
        Add-Content -Path $logFile -Value "  [OK] ciclo concluido com sucesso (off + on)`n"
    } elseif ($onOk) {
        Add-Content -Path $logFile -Value "  [AVISO] ciclo concluido com 'off' falho mas 'on' recuperou (gerador ativo)`n"
    } else {
        Add-Content -Path $logFile -Value "  [ERRO] ciclo falhou -- gerador pode estar desligado, verifique manualmente`n"
    }
}
