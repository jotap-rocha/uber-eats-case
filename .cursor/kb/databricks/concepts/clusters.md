# Databricks Clusters

> **Purpose**: Understand all cluster types, autoscaling, instance pools, Photon, spot instances, cluster policies, and init scripts
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

A Databricks cluster is a set of compute resources (driver + worker nodes) that run Spark workloads. Cluster type determines cost, lifecycle, and configuration. All-purpose clusters are for interactive development; job clusters are for production workloads and terminate after the job completes.

## Cluster Types Comparison

| Feature | All-Purpose | Job Cluster | SQL Warehouse |
|---------|-------------|-------------|---------------|
| Purpose | Dev/notebooks | Production jobs | SQL queries/BI |
| Lifecycle | Manual start/stop | Auto-terminate | Auto-suspend |
| Cost | Higher (idle time) | Lower | Pay-per-query |
| Shared by multiple users | Yes | No | Yes |
| Supports notebooks | Yes | No | No |

## Single-Node vs Multi-Node

```python
# Single-node cluster — no workers, driver only
# Use for: small datasets, local testing, pandas workloads, ML inference
# spark.conf:
#   spark.master = local[*, 4]

# Multi-node — driver + N workers
# Use for: distributed Spark, large datasets, parallel ML training
# Driver node: manages DAG, coordinates tasks (needs RAM, not CPU)
# Worker nodes: execute tasks (need CPU + RAM proportional to data)
```

## Autoscaling

```python
# Standard autoscaling — scales based on pending tasks
# Configured in cluster UI: min_workers=2, max_workers=10

# Enhanced autoscaling (Databricks-optimized)
# Recommended for streaming and DLT pipelines
# Scales down more aggressively when workers are idle
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")

# Cluster config (via API / DABs)
{
  "autoscale": {
    "min_workers": 2,
    "max_workers": 10
  }
}
```

## Instance Pools

```python
# Instance pools keep VMs pre-allocated — reduces startup time from ~5min to ~30sec
# Pool maintains idle VMs (you pay for idle pool VMs)

# Cluster attaches to pool:
{
  "instance_pool_id": "pool-xxxxx",
  "driver_instance_pool_id": "pool-xxxxx"  # optional: separate driver pool
}

# Best practice: use pools for jobs that run frequently (< 30 min interval)
# Not worth it for jobs running less than once per hour
```

## Photon Engine

```python
# Photon is a native C++ vectorized query engine replacing Spark's JVM engine
# Automatically enabled on Photon runtime clusters
# Provides 2-12x speedup for SQL + Delta operations

# Benefits most:
#   - SQL queries (SELECT, GROUP BY, JOIN, aggregations)
#   - Delta Lake reads/writes
#   - DBSQL workloads

# Does NOT help with:
#   - Custom Python UDFs (still JVM/Python)
#   - RDD operations
#   - Complex ML model training (GPU workloads)

# Enable Photon in cluster config:
# Runtime: "Databricks Runtime x.y Photon"
```

## Spot Instances Strategy

```python
# Spot instances = cheaper VMs (50-90% discount) that can be interrupted

# Recommended pattern for jobs:
# - Driver: on-demand (never interrupted — driver loss kills job)
# - Workers: spot instances (if interrupted, task is retried on new worker)

# Job cluster config with spot workers:
{
  "driver_node_type_id": "i3.xlarge",
  "node_type_id": "i3.xlarge",
  "aws_attributes": {
    "availability": "SPOT_WITH_FALLBACK",  # Falls back to on-demand
    "spot_bid_price_percent": 100
  }
}
# SPOT_WITH_FALLBACK — tries spot, falls back to on-demand if unavailable
```

## Políticas de cluster e *init scripts*

Continuação: [clusters-policies-init-scripts.md](clusters-policies-init-scripts.md).

## Related

- [concepts/architecture.md](architecture.md)
- [concepts/notebooks.md](notebooks.md)
- [patterns/spark-optimization.md](../patterns/spark-optimization.md)
