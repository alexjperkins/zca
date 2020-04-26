"""Utils for the pipelines module."""


from . import MissingSignal, StaleSignal


def build_missing_signal(record):
    """Builds a `missing` signalfrom `record`."""
    return MissingSignal(record.date, record.price, 'Missing')


def build_stale_signal(record):
    """Builds a `stale` signal from `record`."""
    return StaleSignal(record.date, record.price, 'Stale')
