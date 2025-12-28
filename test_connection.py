# Test de conexão com Databricks Serverless
# Execute este arquivo usando a extensão Databricks para VS Code

from pyspark.sql import SparkSession

# Inicializa SparkSession (automático no Databricks)
spark = SparkSession.builder.getOrCreate()

# Teste 1: Verificar versão do Spark
print("=" * 50)
print("🚀 TESTE DE CONEXÃO DATABRICKS")
print("=" * 50)
print(f"✅ Spark Version: {spark.version}")
print(f"✅ App Name: {spark.sparkContext.appName}")

# Teste 2: Criar um DataFrame simples
data = [
    ("João", "São Paulo", 28),
    ("Maria", "Rio de Janeiro", 32),
    ("Pedro", "Belo Horizonte", 25),
    ("Ana", "Curitiba", 30)
]

columns = ["nome", "cidade", "idade"]
df = spark.createDataFrame(data, columns)

print("\n📊 DataFrame de teste criado:")
df.show()

# Teste 3: Operações básicas
print(f"✅ Total de registros: {df.count()}")
print(f"✅ Média de idade: {df.agg({'idade': 'avg'}).collect()[0][0]:.1f}")

# Teste 4: Verificar catálogos disponíveis (Unity Catalog)
print("\n📁 Catálogos disponíveis:")
try:
    catalogs = spark.sql("SHOW CATALOGS").collect()
    for cat in catalogs:
        print(f"   - {cat[0]}")
except Exception as e:
    print(f"   ⚠️ Unity Catalog não disponível: {e}")

print("\n" + "=" * 50)
print("🎉 CONEXÃO FUNCIONANDO PERFEITAMENTE!")
print("=" * 50)
