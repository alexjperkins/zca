"""Tests for maths stats functions."""


import pytest

from sigalgo.maths.stats import zscore


@pytest.mark.parametrize(
    "val, mean, stdev, expected",
    [
        (1, 2, 1, 1),
        (1, 1, 0, 0),
    ]
)
def test_zscore(val, mean, stdev, expected):
    """Test zscore calc."""
    assert abs(zscore(val, mean, stdev)) == expected
