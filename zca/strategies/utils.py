"""Utils for the strategies module."""


from . import ZScoreSignal


def build_zscore_signal(date, price, signal_name="outlier"):
    """Build `zscore` signal record.
    """
    return ZScoreSignal(date, price, signal_name)
