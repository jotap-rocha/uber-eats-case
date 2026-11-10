"""Fila de ações por instante (F5.5): um processo, um escritor, uma ação por vez."""

from __future__ import annotations

import heapq
import itertools
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Task:
    at: datetime
    name: str
    run: Callable[[], None] = field(compare=False)


class Agenda:
    """Heap por (instante, ordem de chegada): empate no mesmo instante segue a ordem de agendamento."""

    def __init__(self) -> None:
        self._heap: list[tuple[datetime, int, Task]] = []
        self._seq = itertools.count()

    def __len__(self) -> int:
        return len(self._heap)

    def push(self, task: Task) -> None:
        heapq.heappush(self._heap, (task.at, next(self._seq), task))

    def pop(self) -> Task:
        return heapq.heappop(self._heap)[2]

    def peek_time(self) -> datetime | None:
        return self._heap[0][0] if self._heap else None
