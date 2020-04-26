"""Pipelines for `sigalgo`."""


import operator

from .utils import (build_missing_signal,
                    build_stale_signal)

from ..strategies.zscore import ZScoreStrategy


class ZScorePipeline:
    """ZScore pipeline.

    Finds the following `signals`:
        1. State data
        2. Missing data
        3. Outliers
    """
    def __init__(
            self,
            lag=30,
            threshold=3.5,
            staleness_in_days=7,
            strategy=ZScoreStrategy
    ):
        self.lag = lag
        self.threshold = threshold
        self.staleness = staleness_in_days
        self._strategy = strategy(self.lag, self.threshold)

    def pipe(self, data):
        """Pipe `data`  through the pipeline.
        """
        cleaned_data, pre_signals = self._preprocess(list(data))
        signals = self._strategy.process(cleaned_data)

        # sort
        to_check = pre_signals + signals
        to_check.sort(key=operator.itemgetter(0))
        return to_check

    def _preprocess(self, data):
        """Preprocess the data. Cleaning of stale & missing data.

        TODO: Insert into cleaned_data using `bisect` to sort the
              cleaned_data as we iterate through
        """
        psignals = []
        cleaned_data = []

        prev_change = data[0]

        for i, record in enumerate(data):
            if self._check_missing(record):
                psignals.append(build_missing_signal(record))
                continue

            # Check if two data consec data points have gap > staleness
            if data[i-1 or i] == data[i] and i != 1:
                if self._check_staleness(data[i-1], data[i]):
                    psignals.append(build_stale_signal(record))

            # Check if data hasn't changed for > staleness unit of time
            if self._check_staleness(prev_change, record):
                psignals.append(build_stale_signal(record))

            else:
                cleaned_data.append(record)

            # if data changed, update last changed val
            if record.price != prev_change.price:
                prev_change = record

        return cleaned_data, psignals

    def _check_staleness(self, prev_change, current):
        """Checks if more than `staleness` units of time passed between
            `prev_change` and current.
        """
        if (current.date - prev_change.date).days > self.staleness:
            return True

        return False

    @staticmethod
    def _check_missing(current):
        """Checks if `current` is `missing`.

        `missing` is defined as current.price is None
        """
        if current.price is None:
            return True

        return False
