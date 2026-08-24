# 🧪 LAB: Validação do YARN com WordCount

Este laboratório demonstra como validar o funcionamento do YARN executando o clássico exemplo **WordCount** do MapReduce.

---

## 📋 Objetivo

Validar que o cluster Hadoop está funcionando corretamente executando um job MapReduce via YARN.

---

## 📌 Pré-requisitos

| Componente | Status |
|------------|--------|
| HDFS | ✅ Funcionando |
| YARN | ✅ Funcionando |
| ResourceManager | ✅ Ativo em islnx311 |
| NodeManagers | ✅ Ativos nos workers |

Verificar status dos serviços:

```bash
# Verificar processos Java
jps

# Verificar nós do YARN
yarn node -list

# Verificar status do HDFS
hdfs dfsadmin -report
```

---

## 🚀 Passo a Passo

### 1. Criar arquivo de teste local

```bash
cat > /tmp/wordcount-input.txt << 'EOF'
Hadoop is a framework for distributed storage and processing
Hadoop uses HDFS for storage
HDFS is the Hadoop Distributed File System
YARN is the resource manager of Hadoop
MapReduce is a programming model for processing big data
Big data processing with Hadoop is powerful
EOF
```

### 2. Criar diretório no HDFS e fazer upload

```bash
# Criar estrutura de diretórios
hdfs dfs -mkdir -p /user/hadoop/wordcount/input

# Fazer upload do arquivo
hdfs dfs -put /tmp/wordcount-input.txt /user/hadoop/wordcount/input/

# Verificar upload
hdfs dfs -ls /user/hadoop/wordcount/input/
hdfs dfs -cat /user/hadoop/wordcount/input/wordcount-input.txt
```

### 3. Localizar o JAR de exemplos

```bash
# O JAR está em:
ls -la $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar
```

### 4. Executar o WordCount via YARN

```bash
# Remover output anterior (se existir)
hdfs dfs -rm -r -f /user/hadoop/wordcount/output

# Executar o job
yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar \
    wordcount \
    /user/hadoop/wordcount/input \
    /user/hadoop/wordcount/output
```

### 5. Verificar o resultado

```bash
# Listar arquivos de output
hdfs dfs -ls /user/hadoop/wordcount/output/

# Ver o resultado (contagem de palavras)
hdfs dfs -cat /user/hadoop/wordcount/output/part-r-00000
```

---

## 📊 Resultado Esperado

```
Big	1
Distributed	1
File	1
HDFS	2
Hadoop	4
MapReduce	1
System	1
YARN	1
a	2
and	1
big	1
data	2
distributed	1
for	3
framework	1
is	4
manager	1
model	1
of	1
powerful	1
processing	3
programming	1
resource	1
storage	2
the	1
uses	1
with	1
```

---

## 🖥️ Monitoramento via Web UI

Durante a execução do job, você pode acompanhar o progresso em:

| Interface | URL |
|-----------|-----|
| **ResourceManager** | http://islnx311.drmtz.com.br:8088 |
| **Job History** | http://islnx311.drmtz.com.br:8088/proxy/application_XXXX_XXXX/ |

---

## 📈 Métricas do Job Executado

| Métrica | Valor |
|---------|-------|
| **Job ID** | job_1767119736672_0001 |
| **Status** | ✅ SUCCEEDED |
| **Map Tasks** | 1 |
| **Reduce Tasks** | 1 |
| **Input Records** | 6 linhas |
| **Output Records** | 27 palavras únicas |
| **Tempo Total** | ~20 segundos |
| **Bytes Lidos (HDFS)** | 419 bytes |
| **Bytes Escritos (HDFS)** | 233 bytes |

---

## 🔧 Troubleshooting

### Job não inicia

```bash
# Verificar se YARN está rodando
yarn node -list

# Verificar logs do ResourceManager
tail -100 /DATALAKE/var/hadoop/logs/hadoop-*-resourcemanager-*.log
```

### Erro de memória

Se o job falhar por falta de memória, verifique as configurações em `yarn-site.xml`:

```xml
<property>
    <name>yarn.nodemanager.resource.memory-mb</name>
    <value>8192</value>
</property>
<property>
    <name>yarn.scheduler.maximum-allocation-mb</name>
    <value>8192</value>
</property>
```

### Ver logs do job

```bash
# Listar aplicações
yarn application -list -appStates ALL

# Ver logs de uma aplicação específica
yarn logs -applicationId application_XXXX_XXXX
```

---

## 🧹 Limpeza (Opcional)

```bash
# Remover arquivos de teste do HDFS
hdfs dfs -rm -r /user/hadoop/wordcount

# Remover arquivo local
rm /tmp/wordcount-input.txt
```

---

## ✅ Conclusão

Se o job completou com sucesso e você consegue ver o resultado da contagem de palavras, seu cluster Hadoop está funcionando corretamente com:

- ✅ **HDFS** - Armazenamento distribuído
- ✅ **YARN** - Gerenciamento de recursos
- ✅ **MapReduce** - Processamento distribuído

---

## 📚 Outros Exemplos Disponíveis

O JAR de exemplos contém vários outros programas:

```bash
# Listar todos os exemplos disponíveis
yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar
```

Exemplos incluem:
- `pi` - Calcular Pi usando Monte Carlo
- `terasort` - Ordenação de terabytes
- `grep` - Busca de padrões
- `randomwriter` - Gerador de dados aleatórios

---

> 📅 **Data de execução:** 2026-01-02  
> 🖥️ **Cluster:** islnx311, islnx312, islnx313, islnx314  
> 📦 **Versão Hadoop:** 3.3.6

