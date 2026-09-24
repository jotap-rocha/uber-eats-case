# Pendencias - Docker Resource Tuning (dl-2026-09-20-docker-resources)

> Gerado em 2026-09-22, ao final do Dev Loop L2 dl-2026-09-20-docker-resources.
> Trilha completa (decisoes, riscos, licoes) esta no worktree da sessao, branch
> worktree-abstract-riding-quill, em .claude/sdd/dev-loop-runs/dl-2026-09-20-docker-resources/
> (nao esta na branch main ainda).

## O que ja foi feito

- [x] mem_limit/cpus aplicados aos 6 servicos essenciais em docker-compose.yml
      (postgres-ubereats, minio-ubereats, minio-setup, gen-unified, oracle-ubereats, mongo-ubereats)
      -- confirmado: 6 ocorrencias de "mem_limit:" no arquivo.
- [x] Alerta de estagnacao (+0 em 2 snapshots seguidos, ~2h) no
      scripts/shadowtraffic-report-loop.ps1 -- feito no worktree, ainda nao aplicado aqui no
      checkout principal (nao ha WIP conflitante nesse arquivo, pode copiar direto do worktree).
- [x] scripts/README.md documentado: start-infra.ps1 + toggle-shadowtraffic.ps1 on como fluxo
      oficial de geracao economica; risco dos 4 servicos Azure/GCP sem script dedicado -- feito
      no worktree, ainda nao aplicado aqui.
- [x] Decisao: manter .wslconfig em 10GB (nao subir para 14GB) -- validado com RAM real do host
      (~10.1GB usado / 19.9GB total, sem Docker ativo na checagem).
- [x] docker-compose.yml: diff de mem_limit/cpus ja aplicado E COMMITADO aqui no checkout
      principal? -- CONFIRMAR (ultimo passo foi so aplicar via script, commit ainda pendente,
      ver abaixo).

## O que falta

1. [ ] Commitar docker-compose.yml aqui no checkout principal:
       git add docker-compose.yml
       git commit -m "PERF: aplica mem_limit/cpus aos servicos essenciais"

2. [ ] Copiar as mudancas de scripts/shadowtraffic-report-loop.ps1 e scripts/README.md do
       worktree (branch worktree-abstract-riding-quill) para ca -- ainda so existem la.

3. [ ] TESTAR DE VERDADE: ligar o Docker Desktop e rodar
       .\scripts\start-infra.ps1
       .\scripts\toggle-shadowtraffic.ps1 on
       Atencao especial ao oracle-ubereats (mem_limit: 3g) -- se o healthcheck falhar por
       memoria, subir para 4g em docker-compose.yml.

4. [ ] Decidir se/quando commitar o .gitignore (entrada .claude/worktrees/ ja adicionada,
       nao commitada).

5. [ ] (Opcional, fora de escopo) Quando as fases Azure/GCP sairem de prototipagem: mem_limit
5. [ ] (Opcional, fora de escopo) Quando as fases Azure/GCP sairem de prototipagem: mem_limit
       nos 6 servicos nao-essenciais + script toggle-ingestion-azure.ps1/-gcp.ps1.

## Onde esta o historico completo

Branch worktree-abstract-riding-quill, pasta
.claude/sdd/dev-loop-runs/dl-2026-09-20-docker-resources/ -- tem requirements.md, design.md
(com a reversao do .wslconfig documentada), o PROMPT executado, e DEVLOOP_SUMMARY.md com todas
as licoes aprendidas.
