"""Test pipeline utils."""


import pytest

from sigalgo.pipelines import MissingSignal, StaleSignal
from sigalgo.pipelines.utils import (build_missing_signal,
                                     build_stale_signal)


@pytest.mark.parametrize(
    "build_func, expected_instance, expected_signal",
    [
        (build_missing_signal, MissingSignal, 'Missing'),
        (build_stale_signal, StaleSignal, 'Stale'),
    ],
)
def test_build_signal_methods(
        record,
        build_func,
        expected_instance,
        expected_signal
):
    """Test build missing signal.
    """
    signal = build_func(record)
    assert isinstance(signal, expected_instance)
    assert signal.signal == expected_signal
