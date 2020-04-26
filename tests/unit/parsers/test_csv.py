"""Tests for parsers csv."""


from pathlib import Path

import pytest


def test_csv_parser(csv_parser_clean):
    """Tests the CSV Parser.

    NOTE: This is a magic number here (# rows of clean equities),
          ideally this should be better controlled

    TODO: Fixture up a smaller size CSV thats definite
    """
    assert len(list(csv_parser_clean)) == 2087 - 1  # accouting for headers
