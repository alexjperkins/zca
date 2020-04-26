"""Tests for the `zscore` pipeline."""


import datetime

import pytest

from sigalgo.pipelines.zscore import ZScorePipeline
from sigalgo.records import Record


@pytest.fixture
def zscore_pipeline():
    """ZScorePipeline fixture.
    """
    yield ZScorePipeline(lag=15, threshold=3.5, staleness_in_days=7)


def test_pipeline_pipe_raw(zscore_pipeline, outliers_data_raw):
    """Test the pipeline pipe function.

    NOTE: This is very rudimentary, a proper end2end test
          should be done under the `functional` test namespace
    """
    signals = zscore_pipeline.pipe(outliers_data_raw)
    assert len(signals) > 39


def test_pipeline_pipe_clean(zscore_pipeline, outliers_data_clean):
    """Test the pipeline pipe function.
    """
    signals = zscore_pipeline.pipe(outliers_data_clean)
    assert len(signals) < 30


def test_check_staleness(record, zscore_pipeline):
    """Test for checking staleness.
    """
    assert zscore_pipeline._check_staleness(record, record) == False

    record2 = Record(record.date + datetime.timedelta(days=8), 0.0)

    assert zscore_pipeline._check_staleness(record, record2) == True


def test_check_missing(zscore_pipeline, record, missing_record):
    """Test for checking `missing` data.
    """
    assert zscore_pipeline._check_missing(record) == False
    assert zscore_pipeline._check_missing(missing_record) == True
