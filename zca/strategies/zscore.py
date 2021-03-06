"""Zscore Strategy module."""


import statistics

from .core import BaseStrategy
from .utils import build_zscore_signal as build_signal

from ..maths.stats import zscore
from ..structures import MovingWindow


class ZScoreStrategy(BaseStrategy):
    """Strategy that implements a `smoothed zscore` algorithm for peak finding.

    lag:        the lag for the smoothing `function`,
                also the size of the moving window
    threshold:  x * standard deviations for signal to trigger
    """
    def __init__(self, lag, threshold):
        self.lag = lag
        self.threshold = threshold

    def process(self, data):
        """Process the data. Find signals and return as a list.
        """
        mw, signals = self._init_moving_window(data)
        for rec in data[self.lag:]:
            z = zscore(rec.price, mw.mean(), mw.stdev())
            if abs(z) > self.threshold:
                signals.append(build_signal(rec.date, rec.price))

            mw.shift(rec.price)  # dequeue last item, enqueue new item

        return signals

    def _init_moving_window(self, data):
        """Initializes the opening window, parses potential singals if found.
        """
        mw = MovingWindow(self.lag)
        starting_mw = data[0: self.lag-1]
        mw.init(values=[rec.price for rec in starting_mw])

        # calc potential signals in initial moving window
        prices = [rec.price for rec in starting_mw]
        mean = statistics.mean(prices)
        stdev = statistics.stdev(prices)
        zscores = [zscore(rec.price, mean, stdev) for rec in starting_mw]
        potential_signals = [idx for idx, zscore in enumerate(zscores)
                             if zscore > self.threshold]

        return mw, [starting_mw[idx] for idx in potential_signals]
