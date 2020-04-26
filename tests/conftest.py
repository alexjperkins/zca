"""Common fixtures for sigalgo tests."""


import datetime
import operator
from unittest.mock import MagicMock

import pytest

from pathlib import Path

from sigalgo.parsers.csv import CSVParser
from sigalgo.records import Record
from sigalgo.records.streams import RecordStream


@pytest.fixture
def csv_parser_clean():
    """Fixture for `CSVParser` with clean data.
    """
    path = Path(__file__).parent / "unit/fixtures/clean/FX_history_clean.csv"
    parser = CSVParser(path)
    yield parser


@pytest.fixture
def csv_parser_raw():
    """Fixture for `CSVParser` with raw data.
    """
    path = Path(__file__).parent / "unit/fixtures/raw/FX_history_raw.csv"
    parser = CSVParser(path)
    yield parser


@pytest.fixture
def mocked_csv_parser(mocker):
    """Fixture for `CSVParser` with raw data.
    """
    parser = CSVParser("we don't care")
    mocker.path('open.__enter__', return_value=MagicMock)
    yield parser


@pytest.fixture(name="datetime_obj")
def _datetime_obj():
    """Datetime object fixture.
    """
    yield datetime.datetime.strptime('01/03/2020', '%d/%m/%Y')


@pytest.fixture(name="record")
def _record(datetime_obj):
    """Record fixture.
    """
    yield Record(date=datetime_obj, price=10.0)


@pytest.fixture(name="missing_record")
def _missing_record(datetime_obj):
    """Missing Record fixture.
    """
    yield Record(date=datetime_obj, price=None)


@pytest.fixture
def outliers_data_clean(csv_parser_clean):
    """Fixture for outliers data.
    """
    yield sorted(
        list(RecordStream(csv_parser_clean).parse()),
        key=operator.itemgetter(0)
    )


@pytest.fixture
def outliers_data_raw(csv_parser_raw):
    """Fixture for outliers data.
    """
    yield sorted(
        list(RecordStream(csv_parser_raw).parse()),
        key=operator.itemgetter(0)
    )
