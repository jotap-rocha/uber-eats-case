# Pattern — PyODBC: modo de escrita SQL Server (APPEND vs Overwrite + TRUNCATE)

> **Quando usar:** pipeline grava dados no **SQL Server** via **PyODBC** (INSERT em destino relacional).
> **Gate humano obrigatório** em SDD `/define`, `/design` e Dev Loop `requirements`/`design`/`craft`.

---

## Decisão 1 — APPEND ou Overwrite?

**Pergunta ao utilizador (obrigatória):** *A carga no SQL Server será **APPEND** ou **Overwrite**?*

| Modo | Comportamento | Quando usar | Riscos |
|------|---------------|-------------|--------|
| **APPEND** | Insere linhas **sem** apagar dados existentes | Histórico incremental, auditoria, múltiplas cargas no mesmo dia | Duplicados se re-run sem controlo de idempotência |
| **Overwrite** | **Substitui** o conteúdo lógico da tabela destino (política depende de `truncate`) | Snapshot diário, recarga completa de dimensão/fact | Perda de histórico se mal configurado |

Documentar a escolha no DEFINE/DESIGN/Dev Loop requirements com **justificativa de negócio**.

---

## Decisão 2 — Se Overwrite: `truncate=true` ou `truncate=false`?

**Só aplicável se Decisão 1 = Overwrite.**

**Pergunta ao utilizador (obrigatória):** *No Overwrite, `truncate` será **true** ou **false**?*

| `truncate` | Comportamento típico | Impacto no objeto SQL Server |
|------------|---------------------|------------------------------|
| **`true`** | Drop/recreate ou equivalente agressivo | **Risco alto:** pode **dropar** a tabela e **recriá-la** — tipos originais (INT, DATETIME, DECIMAL…) podem virar **STRING** genérica; perde-se definição, constraints, índices e metadados |
| **`false`** ✅ **boas práticas** | Delete dos dados + **mantém** definição da tabela | **Recomendado:** reutiliza schema, tipos e constraints já criados; Overwrite limpa **dados** e reinsere com a definição **actual** da tabela |

### Por que `truncate=false` é a boa prática?

1. **Preserva DDL** — colunas, tipos, PK/FK, índices definidos previamente (migrations/DBA).
2. **Evita regressão de tipos** — recreate “cego” tende a inferir tudo como string.
3. **Operação reversível** — delete + insert é mais previsível que drop + create.
4. **Alinhado a pipelines corporativos** — tabela destino é **contrato** gerido à parte da carga.

### Quando `truncate=true` seria aceitável?

- Ambiente **DSV** descartável, tabela efémera, **sem** constraints.
- DDL gerido **no mesmo** job de carga (raro; documentar explicitamente).
- **Nunca** PRD sem aprovação DBA + registo no contrato.

---

## Registo obrigatório no artefato

Secção **`## PyODBC — modo de escrita SQL Server`**:

```markdown
| Parâmetro | Valor escolhido | Decidido por | Data |
|-----------|-----------------|--------------|------|
| Modo carga | APPEND \| Overwrite | {nome} | {YYYY-MM-DD} |
| truncate (se Overwrite) | N/A \| true \| false | {nome} | {YYYY-MM-DD} |

**Implicações aceites:** {texto}
**Idempotência / re-run:** {texto}
```

Se Overwrite + `truncate=true` em PRD → **SHOULD** escalar para revisão DBA (finding no pipeline review).

---

## Checklist implementação

- [ ] Modo APPEND/Overwrite **explícito** no código/config (não default implícito)
- [ ] Se Overwrite: `truncate=false` salvo excepção documentada
- [ ] Teste DSV com re-run (APPEND duplica? Overwrite idempotente?)
- [ ] Contrato documenta grain e política de recarga

---

## Referências

- Mandatos: `.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml` → categoria `pyodbc_sqlserver`
- Template decisão: `.cursor/sdd/templates/PYODBC_WRITE_MODE_GATE.md`
- Lane review: `idempotency_reprocessing` (PYODBC-M*)
