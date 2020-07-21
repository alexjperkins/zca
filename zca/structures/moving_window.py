import collections
from typing import Optional
import statistics

from ..domain.models import TransactionalRecord
from .exceptions import (
    MovingWindowFullError,
    MovingWindowInitializationError
)


class TransactionalMovingWindow:
    def __init__(self, max_size):
        self._max_size = max_size
        self._queue = collections.deque(maxlen=self._max_size)

    def __len__(self):
        return len(self._queue)

    def _enqueue(
        self, *, value: TransactionalRecord
    ) -> Optional[TransactionalRecord]:

        if len(self) >= self._max_size:
            raise MovingWindowFullError

        self._queue.appendleft(value)
        return len(self)

    def _dequeue(self):
        if self._queue:
            return self._queue.pop()

        return None

    def shift_right(self, new_value: float):
        self._dequeue()
        self._enqueue(value=new_value)
        return new_value

    def peak(self):
        return self._queue[-1]

    def stdev(self):
        return statistics.stdev(self._queue)

    def mean(self):
        return statistics.mean(self._queue)

    @property
    def max_size(self):
        return self._max_size
