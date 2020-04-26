"""Test the zscore strategy."""


import pytest

from sigalgo.strategies import ZScoreSignal
from sigalgo.strategies.zscore import ZScoreStrategy


@pytest.fixture
def zscore_strategy():
    """Zscore Strategy fixture.
    """
    yield ZScoreStrategy(lag=15, threshold=3.5)


def test_zscore_process(zscore_strategy, outliers_data_raw):
    """Test the zscore process."""
    signals = zscore_strategy.process(outliers_data_raw[:100])
    assert all(isinstance(signal, ZScoreSignal) for signal in signals)
