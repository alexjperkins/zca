import statistics

from .exceptions import (
    MovingWindowFullError,
    MovingWindowInitializationError
)


class MovingWindow:
    def __init__(self, max_size):
        self._max_size = max_size
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def _enqueue(self, value: float) -> int:
        if len(self) >= self._max_size:
            raise MovingWindowFullError

        self._queue.insert(0, value)
        return len(self)

    def _dequeue(self):
        if self._queue:
            return self._queue.pop()

        return len(self)

    def shift(self, new_value: float):
        self._dequeue()
        self._enqueue(value=new_value)
        return new_value

    def peak(self):
        return self._queue[-1]

    def init(self, values):
        if len(values) <= self._max_size:
            for value in reversed(values):
                self._enqueue(value)

            return len(self)

        raise MovingWindowInitializationError(
            'Number of values exceed the window max size'
        )

    def stdev(self):
        return statistics.stdev(self._queue)

    def mean(self):
        return statistics.mean(self._queue)
