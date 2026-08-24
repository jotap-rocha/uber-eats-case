# Tipos de slide — Icatu Slides

> Mapeamento dos **modelos corporativos** para seções HTML. Nomes alinhados ao sumário do `template_ppt_Icatu.pdf`.

---

## 1. Capa (`slide--icatu-cap`)

**Uso:** abertura da apresentação ou de módulo longo.  
**Elementos:** logo Icatu, título principal (Roboto Black), subtítulo opcional (Regular), faixa geométrica de fundo (ver [layout-and-geometry.md](layout-and-geometry.md)), rodapé com data ou código da trilha.

---

## 2. Sub-capa sem imagem (`slide--icatu-subcap`)

**Uso:** quebra de seção (“TÍTULO DA SESSÃO”).  
**Layout:** título grande + linha de acento **Verde #01** ou **Azul #02**; fundo **Azul #01** ou bloco claro **Azul #03** conforme modelo do PDF.

---

## 3. Sub-capa com imagem (`slide--icatu-subcap-img`)

**Uso:** mesma função da sub-capa, com **foto** à direita ou tela cheia com overlay.  
**Regras:** `object-fit: cover`; contraste do título ≥ WCAG AA sobre a imagem (overlay escuro `rgba(27,49,87,0.55)` se necessário).

---

## 4. Página narrativa (`slide--icatu-narrativa`)

**Uso:** história, contexto, parágrafos corridos.  
**Layout:** coluna única ou duas colunas (texto + callout); manter **90% da altura** preenchida (ver [quality-rules.md](quality-rules.md)).

---

## 5. Página com tópicos (`slide--icatu-topicos`)

**Uso:** listas, bullets, agendas.  
**Elementos:** título + lista com marcadores em **Verde #01** ou numeração em **Azul #02**.

---

## 6. Dados e gráficos (`slide--icatu-dados`)

**Uso:** tabelas, gráficos de barras/linhas, KPIs.  
**Cores de série:** ordem sugerida `#6AA2B9` → `#5FBB48` → `#D5DBE6` (linhas/hachuras) — não introduzir cores fora da paleta.

---

## 7. Frase em destaque (`slide--icatu-frase`)

**Uso:** citação única, mantra, “ESTAMOS AQUI” (como no PDF de trilha).  
**Layout:** tipografia grande, central, com muito respiro; opcional moldura fina `1px solid var(--icatu-azul-02)`.

---

## 8. Finalização (`slide--icatu-fim`)

**Uso:** “Obrigado”, próximos passos, contatos internos.  
**Elementos:** logo, mensagem curta, opcional QR interno (se fornecido pelo time).

---

## Convenção de classes

Prefixe classes com `slide--icatu-*` para não colidir com decks **AIDE** no mesmo repositório.
