# Pipeline em três fases: pré-check → carga → pós-check

> **Decisão de equipa:** em vez de um único “mega-job”, separar **validação antes**, **carga** e **validação depois**, com foco em **diff fonte/destino** e **contagem de linhas**.

## Porquê dividir

| Se falhar… | Ganho |
|------------|-------|
| **Pós-check** | Não re-extrair nem re-transformar tudo — repetir só validação ou rollback guiado. |
| **Carga** | Pré-check já validou diferenças esperadas; menos tempo perdido a diagnosticar “dados errados”. |
| **Pré-check** | Sem escritas no destino — rerun barato. |

## As três tasks (contrato lógico)

1. **Pré-check**  
   - Comparar **fonte** e **destino** (schema, contagem, checksum, watermark, etc.).  
   - Produzir um **resumo acordado** (ex.: dict JSON-serializável) para o job de carga e para auditoria (XCom).

2. **Carga (origem → destino)**  
   - Spark / JDBC / cópia ADLS — **idempotente** por `logical date` / partição (ver conceito de idempotência).  
   - Input: output do pré-check (paths, filtros, lista de tabelas).

3. **Pós-check**  
   - Confirmar que a carga **completou com sucesso**.  
   - Reportar **quantas linhas** foram carregadas (e opcionalmente reconciliar com pré-check).  
   - Falhar de forma **explícita** se contagens ou invariantes de negócio não batem → dispara retries/callbacks.

## Esboço TaskFlow

```python
@dag(schedule="@daily", catchup=False, ...)
def curated_daily():
    @task
    def pre_check(ds_nodash: str) -> dict:
        # diff fonte vs destino para dt=...
        return {"ok": True, "tables": [...], "expected_rows": {...}}

    @task
    def load(payload: dict) -> dict:
        if not payload.get("ok"):
            raise ValueError("pre_check falhou")
        # executar carga idempotente
        return {"job_id": "...", "written_partitions": [...]}

    @task
    def post_check(load_result: dict, pre: dict) -> None:
        # validar contagens / integridade vs pre["expected_rows"]
        ...

    pre = pre_check()
    ld = load(pre)
    post_check(ld, pre)

curated_daily()
```

*(Tipagem e nomes de argumentos adaptados ao projeto; usar macros/`ds` conforme [idempotencia-macros-templates.md](../concepts/idempotencia-macros-templates.md).)*

## Relacionado

- [retries-callbacks-alertas.md](retries-callbacks-alertas.md) — falhas na carga vs na validação.  
- [dynamic-task-mapping.md](dynamic-task-mapping.md) — várias tabelas em paralelo mantendo o mesmo padrão de 3 fases.
