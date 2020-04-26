"""Parsers for the `sigalgo` package."""


from . import Record
from ..utils.timestamps import format_datetime


def build_record_from_csv_row(row: str, record=Record):
    """Builds record from `row`."""
    date, price = row.replace('\n', '').split(',')
    return record(
        date=format_datetime(date),
        price=(lambda _str: float(_str) if _str else None)(price),
    )
