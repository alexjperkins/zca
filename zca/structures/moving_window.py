"""Moving window data structure module."""


import statistics

from .exceptions import (MovingWindowFullError,
                         MovingWindowInitializationError)


class MovingWindow:
    """A `Queue` like implementation for a moving window.
    """
    def __init__(self, max_size):
        self._max_size = max_size
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def _enqueue(self, value: float) -> int:
        """Enqueue a new item.

        Returns the length of the queue after insertion.
        """
        if len(self) >= self._max_size:
            raise MovingWindowFullError

        self._queue.insert(0, value)
        return len(self)

    def _dequeue(self):
        """Removes and returns the last item from the queue.
        """
        if self._queue:
            return self._queue.pop()

        return len(self)

    def shift(self, new_value: float):
        """`Shifts` the moving window right.

        Given a new `value`, first dequeues the queue
        and then enqueues the new value
        """
        self._dequeue()
        self._enqueue(value=new_value)
        return new_value

    def peak(self):
        """`Peak` the last value in the `queue`"""
        return self._queue[-1]

    def init(self, values):
        """Initiliazes the moving window with `values` enqueued.
        """
        if len(values) <= self._max_size:
            for value in reversed(values):
                self._enqueue(value)

            return len(self)

        raise MovingWindowInitializationError(
            'Number of values exceed the window max size'
        )

    def stdev(self):
        """Calculates the standard deviation of the current `window` of values.
        """
        return statistics.stdev(self._queue)

    def mean(self):
        """Calculates the mean of the current `window` of values.
        """
        return statistics.mean(self._queue)
