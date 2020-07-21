import dataclasses
from typing import Any


class Event:
    pass


@dataclasses.dataclass
class ValidTransactionalRecord(Event):
    value: float
    timestamp: str
    stdev_delta: float


@dataclasses.dataclass
class Outlier(Event):
    value: float
    timestamp: str
    stdev_delta: float


@dataclasses.dataclass
class InvalidTransactionnalRecord(Event):
    value: Any
    timestamp: str
