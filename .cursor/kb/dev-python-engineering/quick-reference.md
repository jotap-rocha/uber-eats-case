# dev-python-engineering — referência rápida

> **MCP Validated:** 2026-05-06

## Ferramentas de perfil

| Ferramenta | Quando usar |
|------------|-------------|
| `cProfile` / `snakeviz` | Visão global: funções mais custosas |
| `line_profiler` | Função específica linha a linha |
| `py-spy` | Produção / processo já a correr (amostragem) |

## Vetorização vs loop

| Situação | Preferir |
|----------|----------|
| Grande `DataFrame`/`Series` | Operações vetorizadas / expressões do motor |
| Lógica por linha inevitável | `map_partitions`, UDF só se indispensável |
| Muitas colunas temporárias | Encadear sem copiar à toa; revisar dtypes |

## Fronteira de dados

| Camada | Exemplo |
|--------|---------|
| Ficheiro/API → código | Pandera / contrato de schema |
| Config / env | pydantic `BaseSettings` ou modelo dedicado |
| Saída para downstream | Mesmo contrato na escrita ou teste de snapshot |

## Memória

| Evitar | Preferir |
|--------|----------|
| `float64` por defeito em tudo | `float32`, `Int32`, categorias quando Cardinalidade baixa |
| Carregar dataset inteiro | Chunks, lazy scan, generators na ingestão textual |
| `.copy()` em cadeia | Saber se é view; consolidar mutações |

## I/O

| Ponto | Boas práticas |
|-------|----------------|
| Formato analítico | Parquet (colunar), particionar por chaves de filtro |
| Repetição | Cache intermediário ou uma única passagem planeada |
| Compressão | Balancear CPU vs rede/disco com dados representativos |

## Paralelismo

| Tipo de trabalho | Modelo típico |
|------------------|----------------|
| I/O (HTTP, disco local) | `asyncio` ou threads no mesmo processo |
| CPU puro em Python | `multiprocessing`, joblib, ou ferramenta de cluster |
| CPU em dados grandes | Dask, Ray, Spark — dados já particionados |

## Ambiente

| Peça | Notas |
|------|--------|
| Lockfile | `uv.lock`, `poetry.lock`, ou `requirements.txt` gerado por pip-tools |
| Runtime prod | Imagem com mesmas versões minor que o cluster/airgap |

## Testes

| Alvo | Tipo |
|------|------|
| Função pura de transformação | Unitário + casos limite |
| Invariantes amplas | Hypothesis / propriedades quando ROI claro |
| Regressão de job | Smoke em subconjunto + tempo/memória budget |

## Armadilhas comuns

| Não | Sim |
|-----|-----|
| Otimizar sem perfil | Baseline + hotspot antes de mudar |
| `print` em pipeline | `logging` com nível e contexto estruturado |
| Tipagem só “para IDE” em APIs públicas | Contratos também na fronteira dos dados |

## Ligações

| Documento | Caminho |
|-----------|---------|
| Índice completo | `index.md` |
