"""Relógio injetado do simulador (F5.6): histórico o mais rápido possível, depois tempo real.

Todo instante de negócio é hora de Brasília sem fuso (F0, decisão 3). O Brasil não tem horário de
verão desde 2019, então UTC-3 fixo basta e dispensa a base de fusos no Windows.
"""

from __future__ import annotations

import logging
import threading
from collections.abc import Callable
from datetime import datetime, timedelta, timezone

log = logging.getLogger(__name__)

BRT = timezone(timedelta(hours=-3), "America/Sao_Paulo")
MAX_SLEEP_S = 30.0  # acorda de tempos em tempos para atender a parada limpa


def wall_now() -> datetime:
    return datetime.now(BRT).replace(tzinfo=None)


class SimClock:
    """Tempo simulado que nunca passa do relógio de parede: no histórico salta, no tempo real espera.

    `sleep(segundos)` devolve True quando a parada foi pedida (o mesmo contrato de Event.wait).
    """

    def __init__(
        self,
        start: datetime,
        wall: Callable[[], datetime] = wall_now,
        sleep: Callable[[float], bool] | None = None,
    ) -> None:
        self._now = start
        self._wall = wall
        self._stop = threading.Event()
        self._sleep = sleep or self._stop.wait
        self._realtime_logged = False

    @property
    def now(self) -> datetime:
        return self._now

    @property
    def realtime(self) -> bool:
        return self._now >= self._wall()

    def stop(self) -> None:
        self._stop.set()

    def advance_to(self, target: datetime) -> bool:
        """Avança até `target` (nunca volta). False se a parada foi pedida antes de chegar."""
        if target <= self._now:
            return True
        while True:
            remaining = (target - self._wall()).total_seconds()
            if remaining <= 0:
                break
            if not self._realtime_logged:
                log.info("histórico alcançou o relógio de parede em %s: tempo real", self._now)
                self._realtime_logged = True
            if self._sleep(min(remaining, MAX_SLEEP_S)):
                return False
        self._now = target
        return True
