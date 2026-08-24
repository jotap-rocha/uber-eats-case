# Links de Acesso (Cluster)

## Resumo bem pequeno do passo
Links das interfaces web do HDFS/YARN (Hadoop), Spark (History Server), Airflow, Airbyte e workers (DataNode / NodeManager).

## Contexto técnico — BIG-IP (F5) e endpoints amigáveis

Os hostnames `datadriven-<serviço>.icatuseguros.com.br` existem em razão de um **ADC (Application Delivery Controller) F5 BIG-IP** posicionado na frente dos serviços do cluster. Em termos de arquitetura:

- **Virtual Server (VIP):** o BIG-IP expõe um **nome DNS estável** e, em geral, **HTTPS** na borda, em vez de o usuário memorizar `host interno + porta` (ex.: `:9870`, `:8088`, `:18080`, `:8080`).
- **Pool / members:** o tráfego é encaminhado (**reverse proxy / load balancing**) para o backend correto (normalmente o nó **311** para NameNode, ResourceManager e History Server, e o **314** para o Airflow), conforme regras configuradas no LTM.
- **Redirects e reescrita:** onde necessário, o BIG-IP ou políticas associadas tratam **redirecionamentos HTTP→HTTPS**, **ajuste de cabeçalhos** (`Host`, `X-Forwarded-*`) e compatibilidade com UIs que geram links absolutos — o que evita quebras ao sair do acesso “cru” por IP/porta.
- **Benefício operacional:** URL **curta, estável e alinhada ao domínio corporativo**, mais fácil de documentar, liberar em firewall e auditar; o acesso direto aos workers (DataNode / NodeManager) permanece nos hosts `islnx31x` porque costuma ser uso interno de troubleshooting, não passando pelo mesmo padrão de publicação no BIG-IP.

> **Nota:** detalhes de VIP, certificados, SNAT e iRules são mantidos pela equipe de rede/segurança; esta KB registra apenas os **endpoints de consumo** acordados para o time de dados.

## UIs principais (proxy DNS — icatuseguros)

Padrão: `datadriven-<serviço>.icatuseguros.com.br`

```bash
# HDFS NameNode UI
echo "https://datadriven-hdfs.icatuseguros.com.br/"

# YARN ResourceManager UI
echo "https://datadriven-yarn.icatuseguros.com.br/"

# Spark History Server UI
echo "https://datadriven-spark.icatuseguros.com.br/"

# Airflow Webserver UI
echo "https://datadriven-airflow.icatuseguros.com.br/"

# Airbyte UI
echo "https://datadriven-airbyte.icatuseguros.com.br/"
```

Se o URL **HTTPS** falhar no cliente mas o serviço no **314** estiver activo, pode ser **F5/VPN/rede**; **restart** de `airflow-webserver` + `airflow-scheduler` no **314** às vezes ajuda em bloqueios **do próprio Airflow** — ver [`data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md`](data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md) §8.

## DataNode / NodeManager (acesso direto ao host — inalterado)

```bash
# DataNode UI (312/313/314)
echo "http://islnx312.drmtz.com.br:9864/"
echo "http://islnx313.drmtz.com.br:9864/"
echo "http://islnx314.drmtz.com.br:9864/"

# NodeManager UI (312/313/314)
echo "http://islnx312.drmtz.com.br:8042/"
echo "http://islnx313.drmtz.com.br:8042/"
echo "http://islnx314.drmtz.com.br:8042/"
```

## Outros

```bash
# Spark UI (Driver) — porta varia por execução (ex.: 4040); em YARN, preferir proxy do RM
# echo "http://islnx311.drmtz.com.br:4040/"
```
