"""Tests for record streams."""


import pytest

from sigalgo.records import Record
from sigalgo.records.streams import RecordStream


def test_record_stream(csv_parser_clean):
    """Tests the record stream.
    """
    recstream = RecordStream(csv_parser_clean)
    list_recstream = list(recstream)

    assert all(isinstance(list_recstream[i], Record) for i in range(5))
    assert len(list_recstream) == 2087 - 1  # accouting for headers
