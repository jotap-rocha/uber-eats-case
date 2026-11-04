-- Gerado a partir de shared/docs/modelagem/04-modelo-fisico.md (F1.0). Roda uma vez, no init do volume.

CREATE SCHEMA IF NOT EXISTS ubereats;
-- O usuário da aplicação (POSTGRES_USER) enxerga o schema sem qualificar (F1.0 #1).
ALTER ROLE CURRENT_USER SET search_path TO ubereats, public;
SET search_path TO ubereats;

CREATE FUNCTION set_updated_at() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  IF NEW.updated_at IS NOT DISTINCT FROM OLD.updated_at THEN
    NEW.updated_at := localtimestamp;
  END IF;
  RETURN NEW;
END $$;
