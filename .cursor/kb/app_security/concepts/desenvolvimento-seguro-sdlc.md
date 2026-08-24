# Desenvolvimento seguro (SDLC)

> **Purpose**: Segurança no processo — não só no código final.  
> **Confidence**: 0.93

## Pipeline e revisão

- **Code review obrigatório** para mudanças em auth, pagamentos, dados sensíveis e integrações.
- **Secret scanning** no repositório (hooks + CI).
- **Análise de dependências** (SCA) — Snyk, Dependabot, OWASP Dependency-Check; priorizar CVEs com exploit público.
- **SAST** no pipeline para linguagens do projeto.
- **DAST** ou testes de segurança em staging quando viável.

## Ambientes e dados

- **Separação DEV / HML / PRD** — credenciais e dados isolados.
- **Nunca** usar cópias irrestritas de dados reais sensíveis em DEV — anonimizar ou sintetizar.

## Branches e PRs

- Proteger branch principal; exigir aprovações; evitar force-push compartilhado sem política.

## Componentes vulneráveis

- **OWASP Top 10** inclui riscos de **componentes desatualizados** — inventário (SBOM) e cadência de patch.

## Pós-deploy

- Monitoramento de anomalias; resposta a incidentes com playbooks.

## Referências

- OWASP SAMM, OWASP ASVS, NIST SSDF (resumo executivo conforme necessidade da organização).

## Referências cruzadas

- [secrets-gestao.md](secrets-gestao.md), [quick-reference.md](../quick-reference.md)
