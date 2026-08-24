# SSH no cluster Data Lake (311–314)

Documentação para **acesso entre nós** com o utilizador **`hadoop`** (operação no SO). Daemons (ex.: **Airflow** como `airflow`) seguem as regras dos serviços; este guia é para **dev/SRE** em SSH interactivo ou scripts.

---

## Malha de acesso (311 e 314)

Após **chave pública** do host de origem estar em `~/.ssh/authorized_keys` em **todos** os destinos, é possível:

| Origem | Alcança |
|--------|---------|
| **islnx311** | islnx311, islnx312, islnx313, islnx314 |
| **islnx314** | islnx311, islnx312, islnx313, islnx314 |

Ou seja: tanto o **master Hadoop (311)** como o **edge Airflow / dev (314)** podem funcionar como pontos de operações para **correr comandos ou `rsync` em todo o cluster**, desde que as chaves estejam distribuídas.

**Nota:** `~/.ssh` do `hadoop` é **local a cada nó**. Quem precisa de **iniciar** SSH (311 ou 314, ou o teu portátil) tem de ter **par de chaves** e registar a **`.pub`** nos outros — ver secção “Sem senha” abaixo.

---

## Método recomendado

1. **Autenticação:** apenas **chave pública** (sem palavra-passe em scripts).
2. **Algoritmo:** preferir **Ed25519** (`ssh-keygen -t ed25519`); RSA 4096 continua aceitável em ambientes legados.
3. **Cliente SSH:** ficheiro `~/.ssh/config` com `User hadoop`, `IdentityFile` e blocos `Host` por prefixo (`islnx311` … `islnx314` ou `*.drmtz.com.br`) para não repetir opções.
4. **Primeira ligação:** `StrictHostKeyChecking=accept-new` (ou confirmar *host key* por canal seguro); depois `known_hosts` fica estável.
5. **Automação / agents:** `ssh -o BatchMode=yes … comando` — falha imediata se faltar chave (adequado a pipelines).
6. **Ferramentas:** para cópia de árvores (`pyenv`, venvs), usar **`rsync -az`** sobre SSH no utilizador `hadoop`; para ficheiros pontuais, **`scp`**.

Convenção do repositório: o script **`/DATALAKE/workspace/jp/platform/scripts/infra/validate_cluster.sh`** espera correr no **311** com SSH para os quatro nós; o **314** pode usar a **mesma malha** para sincronizar artefactos (ex.: venv `bigdata-py311`) — ver [`python/README.md`](python/README.md).

---

## Configuração SSH sem senha (resumo)

### 1. Gerar par de chaves (na máquina que **inicia** o SSH)

```bash
mkdir -p -m 700 ~/.ssh
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
chmod 600 ~/.ssh/id_ed25519
```

### 2. Distribuir a chave **pública**

Em **cada** destino, como `hadoop`, acrescentar **uma linha** (o conteúdo de `~/.ssh/id_ed25519.pub`) a:

**`~/.ssh/authorized_keys`**

```bash
mkdir -p -m 700 ~/.ssh
chmod 700 ~/.ssh
cat >> ~/.ssh/authorized_keys   # colar a linha da .pub, guardar
chmod 600 ~/.ssh/authorized_keys
```

Alternativa com password na primeira vez (a partir da máquina que tem chave):

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub hadoop@islnx311.drmtz.com.br
# repetir para 312, 313, 314
```

### 3. Validar

```bash
ssh -o BatchMode=yes hadoop@islnx311.drmtz.com.br hostname -s
ssh -o BatchMode=yes hadoop@islnx312.drmtz.com.br hostname -s
ssh -o BatchMode=yes hadoop@islnx313.drmtz.com.br hostname -s
ssh -o BatchMode=yes hadoop@islnx314.drmtz.com.br hostname -s
```

### 4. Rede / DNS

Preferir **DNS** para `islnx*.drmtz.com.br`. **`/etc/hosts`** só como último recurso e de forma **consistente** em todos os nós que participam na malha.

---

## RSA legado (referência)

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@islnx311.drmtz.com.br
# … workers como acima
```

