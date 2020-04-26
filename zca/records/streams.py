"""Parsers for the `sigalgo` package."""


from .utils import build_record_from_csv_row


class RecordStream:
    """Record Stream.
    """
    def __init__(self, stream):
        self._stream = stream

    def __iter__(self):
        """Provide iterable protocol."""
        yield from self.parse()

    def parse(self):
        """Parse and formats the incoming CSV Stream.
        """
        record_stream = (
            build_record_from_csv_row(row) for row in self._stream
        )
        yield from record_stream
