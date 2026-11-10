"""CLI do simulador: python -m simulator run (F5.3, passo 10).

Histórico simulado de `clock.backfill_days` dias e depois tempo real, no mesmo laço. Ctrl-C para
limpo; ligar de novo retoma pelo estado do banco.
"""

from __future__ import annotations

import argparse
import logging
from datetime import datetime

from simulator.clock import wall_now
from simulator.db import Settings, connect_mongo, connect_oracle, connect_postgres
from simulator.engine import (
    bootstrap,
    build_context,
    default_start,
    recover,
    resume_point,
    run,
)
from simulator.params import load_parameters
from simulator.reference import DatabaseLoader

log = logging.getLogger("simulator")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m simulator", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    runner = sub.add_parser("run", help="roda o histórico e depois o tempo real")
    runner.add_argument("--until", type=datetime.fromisoformat, help="para neste instante simulado")
    runner.add_argument("--max-events", type=int, help="para depois de N ações")
    runner.add_argument("--seed", type=int, help="semente do sorteio (reprodutível)")
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
    )

    params = load_parameters()
    settings = Settings.load()
    salts = settings.tracking_salts()
    with (
        connect_postgres(settings) as pg,
        connect_oracle(settings) as ora,
        connect_mongo(settings) as mongo,
    ):
        # Dado sintético e retomada pelo estado do banco: relaxa só a durabilidade do último
        # instante antes de uma queda (cada transação segue atômica). O fsync por commit no HDD
        # da D: custava mais da metade do tempo de cada ação.
        pg.execute("SET synchronous_commit = off")
        resumed = resume_point(pg)
        row = pg.execute("SELECT EXISTS (SELECT 1 FROM orders)").fetchone()
        has_orders = bool(row and row[0])
        start = resumed or default_start(params, wall_now())
        ctx = build_context(
            pg, DatabaseLoader(pg, ora, mongo), params, start=start, seed=args.seed, salts=salts
        )
        log.info("%s em %s", "retomando" if has_orders else "começando", start)
        bootstrap(ctx)
        if has_orders:
            recover(ctx)
        try:
            done = run(ctx, until=args.until, max_events=args.max_events)
        except KeyboardInterrupt:
            ctx.clock.stop()
            done = -1
            log.info("parada pedida; o estado no banco está consistente (uma transação por ação)")
        log.info("fim em %s (%d ações)", ctx.now, done)
        for name, count in sorted(ctx.stats.items()):
            log.info("  %s: %d", name, count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
