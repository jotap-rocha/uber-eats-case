# JAVA_HOME (Hadoop/Spark)

## Resumo bem pequeno do passo
Definir `JAVA_HOME` (Java 11) para que Hadoop e Spark encontrem o Java corretamente.

## Passo (código)

```bash
# Descobrir o JAVA_HOME correto
export JAVA_HOME="$(readlink -f "$(which java)" | sed 's|/bin/java$||')"
echo "$JAVA_HOME"

# Persistir para o usuário (hadoop)
grep -q '^export JAVA_HOME=' ~/.bashrc || cat >> ~/.bashrc << EOF

# Java 11 (Big Data)
export JAVA_HOME=$JAVA_HOME
export PATH=\$JAVA_HOME/bin:\$PATH
export JRE_HOME=\$JAVA_HOME
EOF

source ~/.bashrc

# Validar
echo "$JAVA_HOME"
$JAVA_HOME/bin/java -version
```

