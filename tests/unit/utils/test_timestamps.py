"""Test timestamps utils."""


import datetime

import pytest

from sigalgo.utils.timestamps import format_datetime


@pytest.mark.parametrize(
    "date_str, format_str",
    [
        ('2020/04/01', '%Y/%m/%d'),
        ('03/01/2020', '%d/%m/%Y'),
    ]
)
def test_format_datetime_formatting(date_str, format_str):
    """Test format_datetime creates datetime object."""
    dt = format_datetime(date_str, format_str)
    isinstance(dt, datetime.datetime)


def test_format_datetime_parsing():
    """Test format_datetime parses string correctly."""
    date_str = '03/01/2020'
    dt = format_datetime(date_str)
    isinstance(dt, datetime.datetime)

    assert dt.day == 3
    assert dt.month == 1
    assert dt.year == 2020
