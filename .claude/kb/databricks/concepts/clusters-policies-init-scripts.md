# Clusters — políticas e *init scripts*

> **Purpose**: Extensão de [clusters.md](clusters.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Cluster Policies

```json
{
  "cluster_type": {
    "type": "fixed",
    "value": "job"
  },
  "autoscale.max_workers": {
    "type": "range",
    "maxValue": 20,
    "defaultValue": 5
  },
  "node_type_id": {
    "type": "allowlist",
    "values": ["i3.xlarge", "i3.2xlarge"],
    "defaultValue": "i3.xlarge"
  },
  "spark_version": {
    "type": "regex",
    "pattern": "15\\..*-scala2\\.12",
    "defaultValue": "15.4.x-scala2.12"
  }
}
```

## Init Scripts

```bash
#!/bin/bash
apt-get install -y libgomp1
pip install custom-library==1.2.3
echo "export JAVA_OPTS='-Xmx8g'" >> /etc/environment
```

## Related

- [clusters.md](clusters.md)
