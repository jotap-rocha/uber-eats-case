# Spark 3.5.2 (on YARN)

## Resumo bem pequeno do passo
Extrair o Spark 3.5.2 em `/DATALAKE/opt`, replicar para os nós e validar execução via `--master yarn`.

## Passo (código)

```bash
# 1) (311) Extrair e criar symlink
cd /DATALAKE/opt
tar -xzf /DATALAKE/downloads/spark-3.5.2-bin-hadoop3.tgz
ln -sfn /DATALAKE/opt/spark-3.5.2-bin-hadoop3 /DATALAKE/opt/spark

# 2) (311) Variáveis de ambiente
cat >> ~/.bashrc << 'EOF'

# ====================================
# Spark 3.5.2 (on YARN)
# ====================================
export SPARK_HOME=/DATALAKE/opt/spark
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
EOF
source ~/.bashrc

# 3) (311) spark-env.sh (aponta Java e configs do Hadoop/YARN)
cd $SPARK_HOME
cp -n conf/spark-env.sh.template conf/spark-env.sh 2>/dev/null || true
cat >> conf/spark-env.sh << 'EOF'

# ====================================
# Spark on YARN - Environment
# ====================================
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.25.0.9-7.el9.x86_64
export HADOOP_CONF_DIR=/DATALAKE/opt/hadoop/etc/hadoop
export YARN_CONF_DIR=/DATALAKE/opt/hadoop/etc/hadoop
EOF

# 4) (311) spark-defaults.conf (default para YARN em modo client)
cp -n conf/spark-defaults.conf.template conf/spark-defaults.conf 2>/dev/null || true
grep -q '^spark.master' conf/spark-defaults.conf || cat >> conf/spark-defaults.conf << 'EOF'

# ====================================
# Spark defaults (YARN)
# ====================================
spark.master yarn
spark.submit.deployMode client
EOF

# 5) (311 -> 312/313/314) Replicar binários e configs
for h in islnx312.drmtz.com.br islnx313.drmtz.com.br islnx314.drmtz.com.br; do
  ssh $h 'mkdir -p /DATALAKE/opt'
  rsync -a --delete /DATALAKE/opt/spark-3.5.2-bin-hadoop3/ $h:/DATALAKE/opt/spark-3.5.2-bin-hadoop3/
  ssh $h 'ln -sfn /DATALAKE/opt/spark-3.5.2-bin-hadoop3 /DATALAKE/opt/spark'
  rsync -a /DATALAKE/opt/spark/conf/ $h:/DATALAKE/opt/spark/conf/
  ssh $h 'grep -q \"# Spark 3.5.2 (on YARN)\" ~/.bashrc || cat >> ~/.bashrc << \"EOF\"

# ====================================
# Spark 3.5.2 (on YARN)
# ====================================
export SPARK_HOME=/DATALAKE/opt/spark
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
EOF'
done

# 6) (311) Validar execução no YARN (SparkPi)
$SPARK_HOME/bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master yarn \
  --deploy-mode client \
  $SPARK_HOME/examples/jars/spark-examples_2.12-3.5.2.jar \
  5
```

## Identidade por desenvolvedor (`usr_spark_<slug>`)
Com submit como **`hadoop`**, o YARN regista o mesmo utilizador Unix. Para identificar **quem** disparou o job no RM / History Server, usar:

- **`--name usr_spark_<slug>_nome_do_job`** (define `spark.app.name`), e/ou
- **`--conf spark.yarn.tags=owner=<slug>`** (tags pesquisáveis na UI do YARN).

Padrão completo: [`naming_conventions.md`](../../naming_conventions.md).


