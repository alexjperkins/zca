"""Test strategies utils."""


from sigalgo.strategies import ZScoreSignal
from sigalgo.strategies.utils import build_zscore_signal


def test_build_zscore_signal(record):
    """Test a zscore signal built correctly."""
    signal = build_zscore_signal(record.date, record.price)

    assert isinstance(signal, ZScoreSignal)
