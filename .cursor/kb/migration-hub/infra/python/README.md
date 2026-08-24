# Python (Big Data) — 3.11.11 (via venv)

## Resumo bem pequeno do passo
Padronizar Python 3.11.11 fora do Python do SO (3.9), com venv dedicado para o ecossistema Big Data.

## Paths (padrão do projeto)
- **Interpreter 3.11.11 (pyenv)**: `/DATALAKE/opt/pyenv/versions/3.11.11` (em cada nó o `/DATALAKE` é **LV local** — não assumir NFS; após alterar pyenv num nó de referência, **replicar** com `rsync -az /DATALAKE/opt/pyenv/ hadoop@<outro>:/DATALAKE/opt/pyenv/`.)
- **Symlink “current” (jobs/scripts)**: `/DATALAKE/opt/python311` → `/DATALAKE/opt/pyenv/versions/3.11.11`
- **RPM `patch`**: necessário em **cada nó** para `pyenv install` / `python-build` (`dnf install patch`). Script: `workspace/jp/platform/scripts/infra/python/ensure_patch_installed.sh`.
- **PATH pyenv em login**: `/etc/profile.d/pyenv-datalake.sh` (instalar com `scripts/infra/python/install_pyenv_profile_d.sh`); opcionalmente `~/.bashrc.d/50-pyenv-datalake.sh` para shells não-login.
- **Venv (Big Data)**: `/DATALAKE/opt/venvs/bigdata-py311`

### Sincronizar pacotes do `bigdata-py311` entre nós

O `/DATALAKE` é **volume local** por máquina: o venv **não** se replica sozinho. Quando o **314** (ou outro nó de referência) tiver o conjunto de pacotes desejado, alinhar os restantes com **`rsync`** por SSH (utilizador **`hadoop`**, malha descrita em [`../ssh_configuration.md`](../ssh_configuration.md)):

```bash
# Executado no nó onde o venv está correcto (ex.: 314), para cada destino:
rsync -az --delete /DATALAKE/opt/venvs/bigdata-py311/ \
  hadoop@islnx311.drmtz.com.br:/DATALAKE/opt/venvs/bigdata-py311/
# repetir para 312 e 313 (omitir o próprio host).
```

Script idempotente no projecto: **`/DATALAKE/workspace/jp/platform/scripts/infra/python/sync_bigdata_venv_from_local.sh`** (corre no nó fonte; exclui o host local da lista).

Validação rápida:

```bash
/DATALAKE/opt/venvs/bigdata-py311/bin/python -c "import pydantic_core, dbt; print('OK')"
```

**Não** sincronizar o venv **`airflow-py311`** para workers sem necessidade explícita — é específico do daemon Airflow no **314**.

## Status
✅ Provisionado em TODOS os nós (311/312/313/314)

### Observação (conectividade)
- **Status atual**: ✅ saída para **PyPI liberada** (teste de `pip download` OK no venv).
- **Nota**: em cenários sem egress, o venv é criado normalmente e o `pip`/`setuptools` vêm via `ensurepip`; upgrades/instalações dependem de mirror interno ou wheelhouse offline.

### pyenv (DSV, `hadoop`)
- **Raiz:** `PYENV_ROOT=/DATALAKE/opt/pyenv` (mesmo caminho em todos os nós; conteúdo **replicado** entre máquinas quando o lake não é NFS.)
- **Versão global (shims):** `pyenv global 3.11.11` — alinhada à migração; com `profile.d` + `pyenv init --path`, `bash -l -c 'python3 -V'` deve mostrar **3.11.11** (não o 3.9 do SO).
- **Ambientes vazios para a esteira DSV:** `dev-standard-python` e `dev-standard-spark` (`pyenv virtualenv 3.11.11 <nome>`). Extras: `pyenv activate dev-standard-spark` e `pip install ...` como de costume.
- **Shell:** `~/.bashrc.d/50-pyenv-datalake.sh` (cópia ou equivalente noutros utilizadores de dev).
- **Build (primeira vez):** em RHEL9, o pacote **`patch`** é necessário para o `python-build` do pyenv (`sudo dnf install -y patch`).

### pyenv / escolha do intérprete para venvs em `prd`
- **pyenv** pode ser usado para instalar e selecionar versões **patch** de Python 3.11.x alinhadas à equipe; a partir daí, `python -m venv` em cada **`/DATALAKE/workspace/prd/<projeto>/venv`** fica sob controle explícito.
- **Não** confundir com o Python do **daemon** Airflow (`/DATALAKE/opt/venvs/airflow-py311`) nem com o venv **global** de dados **`bigdata-py311`** — são papéis diferentes (orquestração vs jobs de projeto vs dbt/ferramentas).
- **`PYTHONPATH` global no Airflow** em geral **não** é necessário se cada task usar o `venv` do projecto com imports resolvidos pelo próprio venv — ver [`../../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md`](../../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md) §5b.
