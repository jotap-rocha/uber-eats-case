# Gate humano — PyODBC escrita SQL Server

> Preencher durante SDD `/define` ou Dev Loop `requirements`/`design` quando houver **INSERT via PyODBC** no SQL Server.
> **Não avançar** para `/design` ou `craft` sem respostas explícitas do utilizador.

---

## Pergunta 1 — Modo de carga

**A carga no destino SQL Server será APPEND ou Overwrite?**

| Opção | Implicação |
|-------|------------|
| **APPEND** | Acrescenta linhas; dados antigos permanecem. Re-run pode duplicar — definir idempotência. |
| **Overwrite** | Substitui conteúdo lógico da tabela. **Ir para Pergunta 2.** |

**Resposta do utilizador:** _____________________  
**Data / responsável:** _____________________

---

## Pergunta 2 — TRUNCATE (só se Overwrite)

**No Overwrite, o parâmetro `truncate` será `true` ou `false`?**

| Opção | Implicação |
|-------|------------|
| **`truncate=false`** ✅ **Recomendado** | Apaga **dados**, **mantém** definição da tabela (tipos, constraints, índices). Overwrite reinsere com schema existente. |
| **`truncate=true`** ⚠️ **Risco** | Pode **dropar** e **recriar** a tabela — colunas podem voltar como **STRING**; perde DDL/constraints. Só DSV efémero com aprovação. |

**Resposta do utilizador:** _____________________  
**Aprovação DBA (se truncate=true em PRD):** _____________________  
**Data / responsável:** _____________________

---

## Resumo registado

```yaml
pyodbc_sqlserver_write:
  mode: append | overwrite          # obrigatório
  truncate: null | true | false     # null se append; false recomendado se overwrite
  target_table: "schema.table"
  environment: dsv | prd
  decided_by: ""
  decided_at: ""
  business_rationale: ""
  idempotency_on_rerun: ""
```

---

## Validação antes de implementar

- [ ] Utilizador respondeu Pergunta 1
- [ ] Se Overwrite: utilizador respondeu Pergunta 2
- [ ] Se Overwrite + truncate=true: excepção documentada (+ DBA se PRD)
- [ ] Decisão copiada para DEFINE/DESIGN ou Dev Loop artifacts
