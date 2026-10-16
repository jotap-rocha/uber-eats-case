---
# Padrão de testes — carrega ao tocar a suíte.
paths:
  - "**/tests/**"
  - "**/*_test.py"
  - "**/test_*.py"
---

# Testes — pytest

A suíte é o gate. O hook de `Stop` roda `pytest -q` e **bloqueia** o fim do trabalho se algo
falhar — então o teste tem que ser real e verde, não decorativo.

- **`pytest` + `pytest-asyncio`** (`asyncio_mode = auto`). Testes async são `async def` direto.
- **Nome:** arquivos `test_*.py`, funções `test_*`. Um arquivo por unidade testada.
- **NUNCA comite teste comentado, `@pytest.mark.skip` sem motivo escrito, ou `assert True`.**
  Um teste desligado em silêncio é pior que nenhum — passa no gate sem proteger nada.
  Se precisa pular, escreva o porquê e abra uma task.
- **Teste os guardrails determinísticos** com força: ferramentas de acesso a dados rejeitam
  operações destrutivas, guardam limites, aplicam filtros obrigatórios. Esses são os invariantes
  declarados no `CLAUDE.md` — cubra-os com testes de regressão.
- **NÃO chame o LLM nem APIs externas em teste.** Faça mock/fake do modelo e dos clientes.
  Teste deve rodar offline, determinístico e rápido.
- **Banco em teste:** use fixture/conexão de teste (SQLite async, banco em memória, etc.),
  não o banco de produção. Nunca teste contra dados reais de produção.
- **Cada bug corrigido vira um teste de regressão.** O erro não pode voltar.
- **Para pipelines de dados:** teste por layer (Bronze / Silver / Gold separados). Valide que
  registros inválidos vão para quarantine e não corrompem a camada seguinte.
