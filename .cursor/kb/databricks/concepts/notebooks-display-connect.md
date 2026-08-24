# Notebooks — display(), Connect e IPython

> **Purpose**: Extensão de [notebooks.md](notebooks.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## display() vs show()

```python
display(df)
display(df.limit(100))
display(spark.sql("SELECT * FROM catalog.schema.my_table LIMIT 50"))
display(pandas_df)
display(matplotlib_figure)
df.show(20, truncate=False)
```

## Databricks Connect (Local IDE to Remote Cluster)

```python
from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()
df = spark.read.table("catalog.schema.my_table")
df.groupBy("category").count().show()
```

## Rich Output with IPython

```python
from IPython.display import HTML, Image, Markdown

display(HTML("<h2 style='color:green'>Pipeline Complete</h2>"))
display(Image(filename="/tmp/chart.png"))
display(Markdown("## Summary\n- Rows processed: 1,234,567\n- Errors: 0"))
```

## Common Mistakes

### Wrong

```python
df.show(100)
```

### Correct

```python
display(df)
```

## Related

- [notebooks.md](notebooks.md)
