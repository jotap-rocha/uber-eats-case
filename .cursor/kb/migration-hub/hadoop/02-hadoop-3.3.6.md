# Hadoop 3.3.6 (HDFS + YARN)

## Resumo bem pequeno do passo
Instala e configura o Hadoop 3.3.6 no cluster (311/312/313/314) usando:
- **Binários**: `/DATALAKE/opt/hadoop-3.3.6` (ativo via symlink `/DATALAKE/opt/hadoop`)
- **Dados/Logs**: `/DATALAKE/var/hadoop`

## Passo (código)

```bash
# (311) 1) Criar diretórios base (binários + dados/logs)
mkdir -p /DATALAKE/opt /DATALAKE/downloads /DATALAKE/var/hadoop/{hdfs/namenode,hdfs/datanode,tmp,logs}

# (311) 2) Extrair o Hadoop 3.3.6 (tarball já baixado)
cd /DATALAKE/opt
tar -xzf /DATALAKE/downloads/hadoop-3.3.6.tar.gz

# (311) 3) Criar symlink "hadoop" apontando para a versão ativa
ln -sfn /DATALAKE/opt/hadoop-3.3.6 /DATALAKE/opt/hadoop

# (311) 4) Exportar variáveis de ambiente do Hadoop (para facilitar uso dos comandos)
cat >> ~/.bashrc << 'EOF'

# ====================================
# Hadoop 3.3.6 (HDFS + YARN)
# ====================================
export HADOOP_HOME=/DATALAKE/opt/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
EOF
source ~/.bashrc

# (311) 5) Configurar JAVA_HOME e diretório de logs do Hadoop
sed -i 's|^# export JAVA_HOME=$|export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.25.0.9-7.el9.x86_64|g' $HADOOP_CONF_DIR/hadoop-env.sh
grep -q '^export HADOOP_LOG_DIR=' $HADOOP_CONF_DIR/hadoop-env.sh || \
  echo 'export HADOOP_LOG_DIR=/DATALAKE/var/hadoop/logs' >> $HADOOP_CONF_DIR/hadoop-env.sh

# (311) 6) Configs: core-site.xml / hdfs-site.xml / yarn-site.xml / mapred-site.xml / workers
cat > $HADOOP_CONF_DIR/core-site.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://islnx311.drmtz.com.br:8020</value>
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/DATALAKE/var/hadoop/tmp</value>
  </property>
</configuration>
EOF

cat > $HADOOP_CONF_DIR/hdfs-site.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///DATALAKE/var/hadoop/hdfs/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///DATALAKE/var/hadoop/hdfs/datanode</value>
  </property>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>
EOF

cat > $HADOOP_CONF_DIR/yarn-site.xml << 'EOF'
<?xml version="1.0"?>
<configuration>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>islnx311.drmtz.com.br</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
EOF

cat > $HADOOP_CONF_DIR/mapred-site.xml << 'EOF'
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
EOF

cat > $HADOOP_CONF_DIR/workers << 'EOF'
islnx312.drmtz.com.br
islnx313.drmtz.com.br
islnx314.drmtz.com.br
EOF

# (311) 7) Replicar para os workers (requer SSH sem senha do 311 -> 312/313/314)
for h in islnx312.drmtz.com.br islnx313.drmtz.com.br islnx314.drmtz.com.br; do
  ssh $h 'mkdir -p /DATALAKE/opt /DATALAKE/var/hadoop/{hdfs/namenode,hdfs/datanode,tmp,logs}'
  rsync -a --delete /DATALAKE/opt/hadoop-3.3.6/ $h:/DATALAKE/opt/hadoop-3.3.6/
  ssh $h 'ln -sfn /DATALAKE/opt/hadoop-3.3.6 /DATALAKE/opt/hadoop'
done

# (311) 8) Formatar NameNode (APENAS 1x, no master)
hdfs namenode -format -force -nonInteractive

# (311) 9) Subir serviços
start-dfs.sh
start-yarn.sh

# (311) 10) Validar (nós e serviços)
hdfs dfsadmin -report | head -50
yarn node -list
```

