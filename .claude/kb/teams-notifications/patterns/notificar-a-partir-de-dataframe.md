# Padrão: notificar a partir de um DataFrame

> **Confiança:** 0.93 · Baseado no padrão **Trilha de Auditoria** do time

## Caso de uso

Após executar o motor de regras, um `DataFrame` `df` contém alertas das últimas 24 horas:

- Se **vazio** → mensagem informativa (“nenhum dado / nenhuma suspeita”).
- Se **com linhas** → tabela em Markdown no corpo do card para o canal Teams.

## Variáveis de webhook

| Cenário | Variável `.env` |
|---------|-----------------|
| Trilha PRD | `URL_WEBHOOK_TRILHA_AUDITORIA_PRD` |
| Trilha DSV | `URL_WEBHOOK_TRILHA_AUDITORIA_DSV` |
| Sentinel / operação geral | `URL_WEBHOOK_SENTINEL` |

## Implementação de referência

```python
import os

import pymsteams
from pyspark.sql import DataFrame


def send_notifications_with_df(
    webhook_url: str,
    df: DataFrame,
    *,
    empty_message: str,
    header_message: str,
    columns: list[str],
    verify_ssl: bool = True,
    max_rows: int = 50,
) -> None:
    """
    Envia card Teams com resumo tabular do DataFrame.

    - Usa collect() apenas até max_rows (evitar OOM no driver).
    - webhook_url: tipicamente os.environ['URL_WEBHOOK_TRILHA_AUDITORIA_PRD'].
    """
    card = pymsteams.connectorcard(webhook_url, verify=verify_ssl)
    rows = df.limit(max_rows).collect()

    if not rows:
        message = empty_message
    else:
        header = " | ".join(columns)
        separator = " | ".join(["---"] * len(columns))
        lines = [header, separator]
        for row in rows:
            lines.append(" | ".join(str(row[c]) for c in columns))
        if df.count() > max_rows:
            lines.append(f"\n_(exibindo {max_rows} de mais linhas; verificar no lake/relatório)_")
        message = header_message + "\n\n" + "\n".join(lines)

    card.text(message)
    card.send()


# --- Exemplo Trilha de Auditoria (PRD) ---
webhook = os.environ["URL_WEBHOOK_TRILHA_AUDITORIA_PRD"].strip()

send_notifications_with_df(
    webhook,
    df,
    empty_message=(
        "Nenhum dado encontrado para alerta Trilha de Auditoria nas últimas 24 horas."
    ),
    header_message=(
        "De acordo com as réguas implementadas no motor de regras auditoria, "
        "tivemos uma ou mais movimentações suspeitas nas últimas 24 horas! Favor, verificar!\n\n"
    ),
    columns=["CPF", "Sistema", "Regua", "SCORE", "Data_Ocorrencia"],
    verify_ssl=False,  # somente se infra exigir; preferir True quando possível
)
```

## Exemplo mínimo (estilo original do time)

Equivalente ao snippet legado, com URL parametrizada:

```python
import pymsteams

URL_WEBHOOK_TRILHA_AUDITORIA_PRD = os.environ["URL_WEBHOOK_TRILHA_AUDITORIA_PRD"].strip()


def send_notifications_with_df(url: str, df) -> None:
    my_teams_message = pymsteams.connectorcard(url, verify=False)
    rows = df.collect()
    if not rows:
        message = "Nenhum dado encontrado para alerta Trilha de Auditoria nas últimas 24 horas."
    else:
        message = (
            "De acordo com as réguas implementas no motor de regras auditoria, "
            "tivemos uma ou mais movimentações suspeitas nas últimas 24 horas! Favor, verificar!\n\n"
        )
        message += "CPF | Sistema | Regua | SCORE | Data_Ocorrencia\n"
        message += "--- | --- | --- | --- | ---\n"
        for row in rows:
            message += (
                f"{row['CPF']} | {row['Sistema']} | {row['Regua']} | "
                f"{row['SCORE']} | {row['Data_Ocorrencia']}\n"
            )
    my_teams_message.text(message)
    my_teams_message.send()


send_notifications_with_df(URL_WEBHOOK_TRILHA_AUDITORIA_PRD, df)
```

## Boas práticas

| Prática | Motivo |
|---------|--------|
| `df.limit(max_rows).collect()` | `collect()` sem limite estoura driver |
| Mascarar CPF em canal amplo | LGPD / política de dados |
| Mensagens distintas vazio vs alerta | Operador entende severidade |
| `verify=False` só com OK de rede | Proxy corporativo; documentar exceção |
| Testar em canal DSV antes de PRD | Evitar alarme falso em produção |

## Sentinel (sem DataFrame)

Para alertas simples (texto fixo ou métrica escalar), usar `URL_WEBHOOK_SENTINEL` com [falha-de-pipeline.md](falha-de-pipeline.md) ou `send_teams_text` de [instalacao-e-secrets.md](instalacao-e-secrets.md).
