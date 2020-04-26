"""Test moving window data structure."""


from contextlib import suppress as do_not_raise
import statistics

import pytest

from sigalgo.structures import MovingWindow
from sigalgo.structures.exceptions import MovingWindowInitializationError


@pytest.fixture
def moving_window():
    """Moving Window Fixture.
    """
    yield MovingWindow(10)


@pytest.fixture
def full_moving_window(moving_window):
    """Fixture for a full moving window.
    """
    # would use numpy to gen specified mean & stdev here
    sample = [1, 3, 5, 2, 3, 5, 5, 4, 2, 8]
    for point in sample:
        moving_window._enqueue(point)

    yield moving_window


@pytest.fixture
def not_full_moving_window(moving_window):
    """Fixture for a not full moving window.
    """
    sample = [1, 3, 5, 2, 3, 5, 5, 4, 2]
    for point in sample:
        moving_window._enqueue(point)

    yield moving_window


def test_shift(full_moving_window):
    """Test the `shift` mechanism of the moving window.
    """
    new_val = 5
    assert full_moving_window.shift(new_val) == new_val

    assert full_moving_window.mean() == 4.2
    assert pytest.approx(full_moving_window.stdev(), 0.01) == 1.813


def test_peak(not_full_moving_window):
    """Tests the `peak` func."""
    assert not_full_moving_window.peak() == 1
    assert not_full_moving_window.peak() == 1  # test val still in queue


@pytest.mark.parametrize(
    "init_window_arr, expected_raises",
    [
        ([x for x in range(16)], MovingWindowInitializationError),
    ]
)
def test_moving_window_init(init_window_arr, expected_raises, moving_window):
    """Test the initialization of the moving window queue."""
    with pytest.raises(expected_raises):
        moving_window.init(init_window_arr)
