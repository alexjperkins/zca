"""Timestamp util functions."""


import datetime


def format_datetime(strdatetime: str, _format='%d/%m/%Y'):
    """Format timestamp of `_format` into datetime object."""
    return datetime.datetime.strptime(strdatetime, _format)
