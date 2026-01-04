# Lakeflow Declarative Pipelines - Core Concepts

> Source: https://docs.databricks.com/aws/en/dlt/concepts

## Overview

Lakeflow Declarative Pipelines is a declarative framework for developing batch and streaming data pipelines in SQL and Python.

## Key Concepts

### 1. Flows
- Foundational data processing concept
- Supports streaming and batch semantics
- Reads data from sources, applies processing logic, writes results
- **Flow types include:**
  - Append
  - Update
  - Complete
  - AUTO CDC
  - Materialized View

### 2. Streaming Tables
- Unity Catalog managed tables
- Can have multiple streaming flows
- Supports AUTO CDC flow type

### 3. Materialized Views
- Batch-oriented Unity Catalog managed tables
- Flows always defined implicitly within view definition

### 4. Sinks
- Streaming targets
- Currently supports:
  - Delta tables
  - Apache Kafka
  - Azure EventHubs

### 5. Pipelines
- Unit of development and execution
- Can contain flows, streaming tables, materialized views, sinks
- Automatically orchestrates execution and parallelization

## Key Benefits

- **Automatic orchestration** - No manual task coordination needed
- **Declarative processing** - Focus on "what" not "how"
- **Incremental processing** - Only processes new/changed data
- **Simplified CDC event handling** - Built-in change data capture
- **Reduced manual coding** - Framework handles complexity

## Technical Foundation

- Runs on Databricks Runtime
- Uses the same DataFrame API as Apache Spark and Structured Streaming
- Integrates with Unity Catalog for governance
