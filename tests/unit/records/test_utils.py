"""Tests record utils."""


import pytest

from sigalgo.records.utils import build_record_from_csv_row


@pytest.mark.parametrize(
    "row_string, expected_month, expected_price",
    [
        ("01/03/2020,6.78\n", 3, 6.78),
        ("01/03/2020,\n", 3, None),  # Missing data case
    ]
)
def test_build_record_from_csv_row(row_string, expected_month, expected_price):
    """Test the records are built correctly.
       Accounting for missing data.
    """
    record = build_record_from_csv_row(row_string)

    assert record.date.month == expected_month
    assert record.price == expected_price
