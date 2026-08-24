## Guia de Excelência: DevOps, Versionamento e CI/CD

### 1. Boas Práticas de Versionamento (Git)

O controle de versão não é apenas um "salvamento", é a linha do tempo da evolução do seu projeto.

* **Estratégia de Branching (Fluxo de Trabalho):**
    * **Trunk-based Development:** Para times ágeis e projetos menores, foque na `main`. Branches de vida curta que são integradas rapidamente.
    * **Gitflow:** Recomendado para projetos que exigem releases versionados e manutenção de versões legadas (`main`, `develop`, `feature/`, `hotfix/`, `release/`).
* **Atomicidade:** Cada commit deve representar uma única unidade lógica de mudança. Evite "megacommit" que altera o backend, corrige um CSS e atualiza o README simultaneamente.
* **Ignorar Arquivos:** O uso rigoroso do `.gitignore` é obrigatório. Nunca versione segredos (chaves de API), arquivos de log, pastas de dependências (`node_modules`, `venv`) ou binários pesados.

### 2. Documentação de Commits (Conventional Commits)

Para que um agente (ou humano) entenda o histórico, use o padrão **Conventional Commits**. Isso permite a geração automática de Changelogs.

**Estrutura:** `<tipo>[escopo opcional]: <descrição curta>`

* **Tipos principais:**
    * `feat`: Uma nova funcionalidade.
    * `fix`: Correção de bug.
    * `docs`: Alterações apenas na documentação.
    * `style`: Alterações que não afetam o sentido do código (espaços, formatação).
    * `refactor`: Mudança de código que não corrige bug nem adiciona funcionalidade.
    * `test`: Adição ou correção de testes.
    * `chore`: Atualização de tarefas de build, pacotes, etc.
    * `infra`: Mudanças específicas nos arquivos Docker, Bash ou Docker Compose.
* **Regra de Ouro:** Use o imperativo no assunto ("add feature" em vez de "added feature"). Mantenha o assunto com no máximo 50 caracteres.

### 3. Estratégias de CI/CD (Integração e Entrega Contínua)

O objetivo é falhar rápido e entregar valor de forma consistente.

* **Pipeline as Code:** Defina seu pipeline em arquivos versionados (YAML).
* **Linting e Estática:** O primeiro passo do CI deve ser rodar Linters (como Flake8 para Python ou ESLint para JS) e ferramentas de análise estática. Se o código estiver "sujo", o pipeline deve quebrar imediatamente.
* **Testes Automatizados:** O pipeline só avança se os testes unitários e de integração passarem.
* **Ambientes Isolados:** Garanta que o deploy ocorra primeiro em um ambiente de *Staging* (idêntico ao de produção) antes de chegar ao usuário final.
* **Segurança (DevSecOps):** Implemente ferramentas de varredura de vulnerabilidades em dependências (como Snyk ou Dependabot) dentro do pipeline.

---
