# Vite 5 Configuration

> **Purpose**: Build config, path aliases, env vars, and dev server setup for SisFraude
> **Confidence**: 0.95
> **MCP Validated:** 2026-04-20

## Overview

SisFraude uses Vite 5 with the `@vitejs/plugin-react-swc` plugin (SWC-based transpilation — faster than Babel). The `@/` path alias is registered in both `vite.config.ts` and `tsconfig.json`. Environment variables must be prefixed with `VITE_` to be accessible in browser code.

## vite.config.ts (actual project config)

Fonte de verdade: **`vite.config.ts` na raiz do repo** (não copiar snippets desatualizados).

Pontos principais:
- **`DEV_SERVER_PORT`** — porta do dev server e do `vite preview`; **default `8443`** se a variável estiver vazia (evita colisão com **nginx na 443** no mesmo host). Override opcional: `8080`, etc.
- **`host`** — default `"localhost"`. Com **`VITE_DEV_BIND_LAN=1`** no `.env`, escuta em todas as interfaces → **`https://<hostname>:8443/`** (ou HTTP sem TLS) na rede.
- **Proxy `/api`** → `http://127.0.0.1:8787` com `timeout` / `proxyTimeout` longos (~30 min) para o Lab Databricks sem `LIMIT`.
- **TLS opcional** — `vite/devTls.ts` + `DEV_TLS_CERT_PATH` / `DEV_TLS_KEY_PATH` quando HTTPS directo no Vite.
- **`hmr.overlay: false`**, **`componentTagger`** só em development — ver arquivo real.

## Path Alias @/

The `@/` alias maps to `src/`. It is configured in two places:

```typescript
// vite.config.ts — runtime resolution
resolve: { alias: { "@": path.resolve(__dirname, "./src") } }
```

```json
// tsconfig.json — TypeScript type resolution
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["./src/*"] }
  }
}
```

Both must be in sync. If you add a new alias, add it to both files.

```tsx
// Always use @/ — never relative paths across src/
import { FraudCase } from "@/types/fraud";          // correct
import { FraudCase } from "../../types/fraud";       // wrong
```

## Environment Variables

Vite only exposes env vars prefixed with `VITE_` to client code. Variables without this prefix are server-only and will be `undefined` in the browser.

```bash
# .env — project env vars
VITE_SUPABASE_URL=https://xxx.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=eyJ...
VITE_SUPABASE_PROJECT_ID=xxx
```

```typescript
// Access in code — use import.meta.env, not process.env
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const anonKey     = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY;

// Type-safe access (Vite injects ImportMetaEnv)
// For custom vars, extend in src/vite-env.d.ts:
interface ImportMetaEnv {
  readonly VITE_SUPABASE_URL: string;
  readonly VITE_SUPABASE_PUBLISHABLE_KEY: string;
}
```

## Build Output

```bash
npm run build    # → dist/ directory
npm run preview  # → serve dist/ (porta = DEV_SERVER_PORT, default 8443)
npm run dev      # → dev server default porta 8443 + HMR
```

## Quick Reference

| Config | Value | Purpose |
|--------|-------|---------|
| Dev port | **`8443`** (default; `DEV_SERVER_PORT`) | Local development; nginx PRD usa **443** |
| `@/` resolves to | `src/` | Path alias |
| Env prefix | `VITE_` | Browser-accessible vars |
| Access pattern | `import.meta.env.VITE_*` | Not `process.env` |
| React plugin | `@vitejs/plugin-react-swc` | SWC transpiler |

## Common Mistakes

### Wrong

```typescript
process.env.VITE_SUPABASE_URL          // undefined in browser
import.meta.env.SUPABASE_URL           // undefined — missing VITE_ prefix
import { X } from "../../lib/utils"    // relative path across src/
```

### Correct

```typescript
import.meta.env.VITE_SUPABASE_URL      // works in browser
import { cn } from "@/lib/utils"       // alias-based import
```

## Related

- [concepts/typescript-patterns.md](typescript-patterns.md) — TypeScript config context
- [concepts/shadcn-ui.md](shadcn-ui.md) — components that use env-based Supabase client
