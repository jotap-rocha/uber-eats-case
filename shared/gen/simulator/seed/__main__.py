"""Linha de comando dos seeds: python -m simulator.seed {cities,catalog,profiles,all} (F5.3)."""

from __future__ import annotations

import argparse
import logging
from datetime import date, timedelta

from simulator.db import Settings, connect_mongo, connect_oracle, connect_postgres
from simulator.params import load_parameters
from simulator.seed.catalog import load_catalog
from simulator.seed.writers import SeedCount, seed_catalog, seed_cities, seed_profiles


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m simulator.seed", description=__doc__)
    parser.add_argument("step", choices=["cities", "catalog", "profiles", "all"])
    parser.add_argument(
        "--start-day",
        type=date.fromisoformat,
        help="dia do restock inicial (padrão: hoje menos clock.backfill_days, F5.6)",
    )
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    params = load_parameters()
    settings = Settings.load()
    start_day = args.start_day or date.today() - timedelta(
        days=int(params.section("clock")["backfill_days"])
    )
    counts: list[SeedCount] = []

    with connect_postgres(settings) as pg:
        if args.step in ("cities", "all"):
            with connect_oracle(settings) as ora:
                counts += seed_cities(pg, ora, params.cities)
        if args.step in ("catalog", "profiles", "all"):
            catalog = load_catalog()
            if args.step in ("catalog", "all"):
                counts += seed_catalog(pg, params, catalog, start_day)
            if args.step in ("profiles", "all"):
                with connect_mongo(settings) as mongo:
                    counts += seed_profiles(pg, mongo, params, catalog)

    for c in counts:
        print(f"{c.target}: {c.written} gravados, {c.skipped} já existiam")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
