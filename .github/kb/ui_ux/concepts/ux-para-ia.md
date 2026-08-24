# UX para IA (agentes e copilotos)

> **Purpose**: Separar *sugestão* de *ação*, e sempre mostrar “como chegamos lá”.  
> **Confidence**: 0.91 (área em evolução rápida)

## Princípios

1. **Mostrar o que o agente está fazendo** — Passos, ferramentas invocadas, “pensando…” com limite de tempo.
2. **Separar resposta de evidência** — Resumo acima; fontes, trechos SQL, links abaixo.
3. **Copiar resposta** — Botão explícito para analistas colarem em ofício/email.
4. **Refazer pergunta** — Manter input editável; “tentar outra formulação”.
5. **Fontes / contexto** — O que entrou no prompt (documentos, casos) enumerado.
6. **Sugestão × ação real** — Labels distintos: “Sugerir classificação” vs “Aplicar classificação”.
7. **Confirmação antes do sensível** — Escrita em banco, e-mail externo, exclusão: human-in-the-loop.

## Confiança calibrada

Indicadores discretos (“alta confiança” só com métrica ou evidência); evitar halucinação silenciosa.

## Auditoria

Quando possível: ID da interação, modelo, versão do prompt — para observabilidade.

## Referências cruzadas

- [seguranca-experiencia.md](seguranca-experiencia.md), `.github/kb/genai/`
