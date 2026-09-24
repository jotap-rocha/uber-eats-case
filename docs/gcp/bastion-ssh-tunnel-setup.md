# Túnel SSH reverso — Fase 3/GCP (bastion + `autossh`)

> Referência: `DESIGN_INGESTAO_GCP_FASE3.md`, Decisão 1. Assumption A-001 do `DEFINE_INGESTAO_GCP_FASE3.md` (estabilidade do túnel) fica sob observação nesta configuração.

## Por que existe

O Datastream é *pull-based* — precisa iniciar a conexão até Postgres/Oracle/MongoDB, que continuam rodando localmente (decisão do brainstorm: não migrar a Fase 0 para uma VM GCP, ao contrário da EC2 da Fase 2/AWS). O bastion (`infra/gcp/fase3-ingestao/bastion.tf`) é uma GCE VM mínima e pública que só encaminha SSH — a máquina local é quem abre e mantém o túnel, não o bastion.

## Passo a passo

1. **Gerar o par de chaves** dedicado ao túnel (não reaproveitar a chave pessoal do operador):

   ```bash
   ssh-keygen -t ed25519 -f ~/.ssh/ubereats_gcp_bastion -N ""
   ```

2. **Provisionar o bastion** via Terraform, passando a chave pública em `bastion_ssh_public_key` e a privada (conteúdo do arquivo) em `bastion_ssh_private_key` — esta última também é usada pelo Datastream na "Forward SSH tunnel connectivity profile" (`datastream.tf`).

3. **Copiar a chave privada** para a máquina local em `/etc/ubereats-gcp/bastion_key` (permissão `600`), e substituir `BASTION_PUBLIC_IP` em `deploy/autossh/ubereats-gcp-tunnel.service` pelo output `bastion_public_ip` do Terraform.

4. **Instalar o `autossh`** na máquina local (`apt install autossh` / `choco install autossh` / WSL) e registrar o serviço:

   ```bash
   sudo cp deploy/autossh/ubereats-gcp-tunnel.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now ubereats-gcp-tunnel.service
   ```

5. **Validar o túnel**, a partir do próprio bastion (via SSH administrativo, `admin_access_cidr`):

   ```bash
   ssh admin@BASTION_PUBLIC_IP "nc -zv localhost 15432 && nc -zv localhost 11521 && nc -zv localhost 27017"
   ```

6. **Confirmar no console do Datastream** que os 3 connection profiles (`postgres-source`, `oracle-source`, `mongo-source`) validam com sucesso ("Run validation") antes de criar os streams.

## Risco aceito (A-001)

Uma queda prolongada da máquina local (não só da rede) interrompe o Datastream até a reconexão — `autossh` com `Restart=always` cobre quedas de rede transitórias, não indisponibilidade da máquina em si. Monitorar a saúde do túnel é recomendado (mandato OBS-M01, SHOULD) mas não há SLA de produção 24/7 que torne isso bloqueante, dado o caráter de portfólio pessoal do projeto.
