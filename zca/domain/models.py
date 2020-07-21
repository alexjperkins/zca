import dataclasses

from structures import TransactionalMovingWindow


@dataclasses.dataclass(unsafe_hash=True)
class TransactionalRecord:
    value: float
    timestamp: str


class History:
    def __init__(self, buffersize: int):
        self.recent_history = TransactionalMovingWindow(
            max_size=buffersize
        )
        self.events = []

    def push(self, *, new_transaction: TransactionalRecord):
        self.recent_history.shift_right(
            new_record=new_transaction
        )
