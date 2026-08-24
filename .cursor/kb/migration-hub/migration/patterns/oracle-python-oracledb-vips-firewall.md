# Oracle — python-oracledb, VIPs e firewall (timeout DPY-6005)

> **Revisão documental:** 2026-05-19  
> **Contexto:** Jobs Python no DATALAKE (ex.: `apex_data_ingestion`) que ligam a Oracle via **`python-oracledb`** (modo thin) + **`SERVICE_NAME`**.  
> **Validado com DBAs:** os IPs extra observados em tentativas de ligação são **VIPs Oracle** (SCAN + VIPs de serviço/nó) — **parte normal do processo**, não “cache” de cluster desativado no código da aplicação.

## Sintoma típico

```text
oracledb.exceptions.OperationalError: DPY-6005: cannot connect to database ... timed out
TimeoutError: timed out  (em socket.connect)
```

Frequentemente **depois** de:

- `nc` / `bash /dev/tcp/<scan>/1521` **OK** no host de origem (ex. `ISLNX314`);
- firewall “liberado” só para o **SCAN** ou para um subconjunto de IPs.

## O que o código da aplicação envia

O job passa **um** host e **um** `SERVICE_NAME` — por exemplo:

```text
HOST=apexprd.drmtz.com.br  (ou scan equivalente)
PORT=1521
SERVICE_NAME=apexprd
```

O DSN `makedsn` tem **um único** `ADDRESS`. **Não** há lista de VIPs no repositório Python.

## Por que aparecem vários IPs na ligação

Com **`SERVICE_NAME`**, o **`python-oracledb` (thin)** e o protocolo Oracle:

1. Ligam ao host inicial (SCAN ou VIP);
2. Consultam o **listener** / resolução de serviço (incl. DNS interno Oracle, quando aplicável);
3. Obtêm **todos os endpoints** associados ao serviço (VIPs de nó, VIPs de serviço, etc.);
4. Tentam **vários destinos em paralelo** (comportamento esperado em RAC / Exadata).

Os IPs adicionais são **VIPs Oracle válidos** do ambiente — **não** indicam, por si só, que a aplicação referencia um “cluster antigo” no código.

| Hipótese incorrecta | Realidade |
|---------------------|-----------|
| “O Python guarda cache de IPs antigos” | Cache de hosts **não** é o mecanismo principal; descoberta é **em tempo de ligação** via serviço/listener |
| “Basta liberar firewall no SCAN” | O cliente pode tentar **outros VIPs** além do SCAN |
| “TCP OK no scan ⇒ Oracle OK” | TCP aberto ≠ handshake Oracle completo; timeouts em **qualquer** VIP bloqueado podem falhar a ligação global |

## Troubleshooting (ordem sugerida)

### 1. Confirmar origem e alvo no ticket

| Campo | Exemplo |
|-------|---------|
| Origem | FQDN + IP do runner (ex. `islnx314.drmtz.com.br`) |
| Destino lógico | SCAN + `SERVICE_NAME` acordado com DBA |
| Porta | **TCP 1521** |

### 2. Teste TCP (rede) — SCAN e VIPs

Pedir à **DBA** a lista de **VIPs** que o serviço usa (não só o SCAN). No host de origem:

```bash
getent hosts <scan-ou-host-oracle>
timeout 3 bash -c 'echo >/dev/tcp/<scan>/1521' && echo OK || echo FAIL
for ip in <vip1> <vip2> <vip3>; do
  timeout 3 bash -c "echo >/dev/tcp/$ip/1521" 2>/dev/null && echo "$ip OK" || echo "$ip FAIL"
done
```

**Todos** os VIPs usados pelo serviço devem responder ou estar **explicitamente liberados** na origem → destino (Guardicore / firewall).

### 3. Teste aplicacional (sem carga de dados)

No projecto Python (ex. `apex_data_ingestion`):

```bash
cd /DATALAKE/workspace/prd/apex_data_ingestion
source .venv/bin/activate
APEX_ORACLE_TCP_CONNECT_TIMEOUT=15 APEX_CONNECTIVITY_TEST=1 \
  python src/jobs/apex_db_version_ingestion_.py
```

Ou teste de integração:

```bash
pytest tests/integration/test_oracle_apexprd_live.py -s -v
```

### 4. Ver endereços tentados (evidência para rede)

```bash
timeout 20 strace -e trace=connect -f python -c "
import oracledb
try:
    oracledb.connect(
        user='...', password='...',
        dsn=oracledb.makedsn('apexprd.drmtz.com.br', 1521, service_name='apexprd'),
        tcp_connect_timeout=10,
    )
except Exception:
    pass
" 2>&1 | grep 'sin_addr'
```

Anexar ao chamado: **todos** os `sin_addr` na porta **1521**, não só o SCAN.

### 5. Escalar para DBA (se TCP OK em todos os VIPs e ainda falha)

- Confirmar **`SERVICE_NAME`** exacto (`apexprd` vs `APEXPRD`);
- Validar listener / registo do serviço;
- Avaliar ligação “pinned” (`INSTANCE_NAME` / SID num nó) se aplicável — **só com orientação DBA**.

## Pedido de liberação (modelo para rede / Guardicore)

> Origem: `<host-runner>` (`<IP>`)  
> Destino: serviço Oracle `<SERVICE_NAME>` — liberar **TCP 1521** para **SCAN + todos os VIPs** fornecidos pela DBA (lista completa, não só um IP).  
> Nota: clientes `python-oracledb` com `SERVICE_NAME` tentam múltiplos VIPs Oracle por desenho; timeout em **um** VIP bloqueado pode causar `DPY-6005`.

## O que **não** resolve

| Acção | Limitação |
|-------|-----------|
| Alterar só o host no Python para um VIP | Listener/serviço pode ainda redirecionar para outros VIPs |
| `tcp_connect_timeout` baixo | Falha mais rápido; **não** ignora VIPs |
| Assumir IPs “extra” = cluster legado | Validar com DBA — são **VIPs** do processo Oracle |

## Relacionado

- [`portacao-de-job.md`](portacao-de-job.md) — checklist de portação de jobs Python  
- [`../quick-reference.md`](../quick-reference.md) — paths DATALAKE  
- Projecto exemplo: `/DATALAKE/workspace/prd/apex_data_ingestion` — `APEX_CONNECTIVITY_TEST=1`, `tests/integration/test_oracle_apexprd_live.py`
