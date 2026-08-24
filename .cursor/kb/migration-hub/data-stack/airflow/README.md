# Airflow (instalado) — Nó 314 (Worker 3)

## Operação no edge — checklist e validação

- **Guia completo (DAGs, `workspace/prd`, dbt→YARN, Connections/Variables, comandos de validação):** [`EDGE-314-OPERACAO-E-VALIDACAO.md`](EDGE-314-OPERACAO-E-VALIDACAO.md)  
- **Cópia espelhada no 314:** `/DATALAKE/workspace/prd/CHECKLIST-EDGE-314.md` e `/DATALAKE/workspace/prd/README.md`
- **Práticas de desenho de DAG (TaskFlow, idempotência, retries, dynamic mapping):** [`airflow/index.md`](../../../airflow/index.md)

## Resumo bem pequeno do passo
Provisionar **Airflow** no nó `ISLNX314` para orquestração de pipelines (ex.: dbt + Spark on YARN).

**Observação:** a instalação foi feita via `pip` com *constraints* oficiais do Airflow (Python 3.11).

## Estratégia recomendada para recursos limitados (agora)
- **Executor**: `LocalExecutor` (mais simples; evita Celery/Redis)
- **Metadata DB**: PostgreSQL local no próprio 314 (SPOF, mas viável para início)
- **Airflow Home**: `/DATALAKE/var/airflow`
- **Venv dedicado**: `/DATALAKE/opt/venvs/airflow-py311` (não misturar com bigdata-py311)

## Versões alvo (fixadas)
- **Airflow**: **2.11.1** (compatível com Python **3.11.11**; instalado com *constraints* oficiais `constraints-2.11.1/constraints-3.11.txt`)
- **PostgreSQL**: **15** (via `dnf module postgresql:15` no RHEL9)

## Status (ambiente atual)
- **Nó 314**
  - **PostgreSQL 15**: ✅ instalado e ativo (metadata DB criado para Airflow)
  - **Usuário `airflow` + dirs + venv**: ✅ provisionado (`/DATALAKE/opt/venvs/airflow-py311`)
  - **Airflow (pacote Python)**: ✅ `apache-airflow[postgres]==2.11.1`; provider **SSH** opcional pinado à mesma constraints (`apache-airflow-providers-ssh`, via [`install_airflow.sh`](/DATALAKE/workspace/jp/platform/scripts/data_stack/airflow/install_airflow.sh))
  - **Systemd**: ✅ `airflow-webserver.service` + `airflow-scheduler.service`
  - **UI (host):** `http://islnx314.drmtz.com.br:8080/`
  - **UI (proxy BIG-IP):** ver [`acess_links.md`](../../acess_links.md) — `https://datadriven-airflow.icatuseguros.com.br/`
  - **Usuário admin (Web / FAB):** `admin`
    - **Senha:** `/DATALAKE/var/airflow/secrets/airflow_admin_password` (ficheiro no servidor; **nunca** em Git)
  - **EnvironmentFile (systemd)**: `/etc/sysconfig/airflow` (root-only)

## Utilizadores FAB cadastrados (314)

Estado reflectido na metadata DB (`ab_user`), **2026-04-30**. Conta **`admin`** existe para bootstrap mas não está listada aqui.

| Username (FAB)       | E-mail                         | Ativo |
|------------------------|--------------------------------|-------|
| `usr_airflow_cadu`     | ceribeiro@icatuseguros.com.br  | sim   |
| `usr_airflow_fabiano`  | fjmorais@icatuseguros.com.br   | sim   |
| `usr_airflow_jp`       | joprocha@icatuseguros.com.br   | sim   |
| `usr_airflow_maria`    | mflores@icatuseguros.com.br    | sim   |

**Nota:** o username `usr_airflow_jp` não segue o sufixo literal do login org `joprocha`; convém manter este quadro alinhado à DB quando criarem novas contas ou renomearem utilizadores.

Para listar no servidor:

```sql
SELECT id, username, email, active FROM ab_user WHERE username <> 'admin' ORDER BY username;
```

## Política de acesso (equipe)
- **Linux (SO):** só **`hadoop`** para SSH e administração de hosts; ver [`naming_conventions.md`](../../naming_conventions.md).
- **Daemons no 314:** processos **`airflow`** (systemd) — inalterado.
- **Web UI (FAB):** **um login por pessoa** no padrão `usr_airflow_<login_organizacional>`, **todos Admin**; lista: [`../../team.md`](../../team.md). Senhas por pessoa fora de Git, no **314** (p.ex. ficheiro por conta em `…/secrets/`; ver *Naming* e script de provisionamento). O utilizador **`admin`** pode permanecer para bootstrap; senha em `…/airflow_admin_password` no 314.
- **E-mail no FAB:** usar endereços **`@icatuseguros.com.br`** (cadastro no metadata DB / tabela `ab_user`); não versionar e-mails pessoais no Git.
- **Criação de utilizadores:** preferir o script idempotente [`provision_team_users.sh`](/DATALAKE/workspace/jp/platform/scripts/data_stack/airflow/provision_team_users.sh) (CSV + ficheiros de senha em `/DATALAKE/var/airflow/secrets/`, **nunca** em Git). Alternativa manual: `airflow users create` como utilizador **`airflow`** no 314 — carregar variáveis de **`/etc/sysconfig/airflow`** (ex.: `sudo bash -c 'set -a; source /etc/sysconfig/airflow; set +a; sudo -u airflow -E ...'`). Se `airflow users create` disser que o papel **User** não existe, correr **`airflow sync-perm`** uma vez com o mesmo padrão de env.
- **Senhas por utilizador FAB:** um ficheiro por conta em `/DATALAKE/var/airflow/secrets/` (ex.: `usr_airflow_jp_password`, `usr_airflow_fabiano_password`, …); alinhar nomes de ficheiro ao `username` do FAB; rotação ao sair da equipe ou em incidente.
- **Boas práticas:** senhas fora do Git; rotação quando alguém sair da equipa; **tasks** continuam no UID **`airflow`** salvo *impersonation* futura.
- **Segredos de integração (canónico):** **OCI Vault** — ver [`naming_conventions.md`](../../naming_conventions.md); ficheiros em `/DATALAKE/var/airflow/secrets/` apenas em transição.

## Portas (referência)
- **Airflow Webserver**: `8080/tcp`
- **PostgreSQL** (se local): `5432/tcp` (recomendado **localhost only** inicialmente)

## UI lenta ou sem resposta — tentar restart (314)

Em sintomas de **webserver ou scheduler presos** (sem evidência de problema de rede), no **`islnx314`**:

```bash
sudo systemctl restart airflow-scheduler.service airflow-webserver.service
```

Esperar **10–15 s** e validar `http://127.0.0.1:8080/` no próprio nó. **Não resolve** bloqueio **VPN → lake** nem falhas do **F5** — ver secção de troubleshooting em [`EDGE-314-OPERACAO-E-VALIDACAO.md`](EDGE-314-OPERACAO-E-VALIDACAO.md) §8.

## UI “Internal Server Error” após upgrade de minor (ex.: 2.9 → 2.11)

Se o **scheduler** estiver OK mas a **UI** devolver 500, verifique o journal (`journalctl -u airflow-webserver`). Erros típicos após mudança de **Flask-Session** / serialização:

- `UnicodeDecodeError: 'utf-8' codec can't decode byte ...` ao ler sessões na tabela `session`
- em cascata: `AttributeError: 'NoneType' object has no attribute 'get'` em `flask_login`

**Correcção:** as sessões antigas na metadata DB são incompatíveis. Limpar apenas a tabela de sessões (utilizadores voltam a autenticar-se; não afecta DAGs nem histórico de tasks):

```bash
sudo -u postgres psql -d airflow -c "TRUNCATE TABLE session;"
sudo systemctl restart airflow-webserver
```

## Nota (SELinux / RHEL)
Em RHEL com SELinux **Enforcing**, arquivos criados via `/tmp` podem herdar contexto incorreto e quebrar o `systemd` (ex.: `Permission denied` ao carregar env/exec).  
Se isso ocorrer, a correção é relabel com `restorecon` e/ou definir `fcontext` persistente com `semanage` para `/DATALAKE/opt` e `/DATALAKE/var`.

## O que dá pra adiantar sem internet
- Criar usuário `airflow`
- Criar diretórios `/DATALAKE/opt/airflow`, `/DATALAKE/var/airflow`, logs
- Criar o venv `airflow-py311` (sem instalar pacotes ainda)
- Provisionar PostgreSQL (initdb, usuário e DB do Airflow) — opcional, mas recomendado para sair do SQLite


