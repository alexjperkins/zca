"""Pipelines for `sigalgo`"""


from collections import namedtuple


StaleSignal = namedtuple('StaleSignal', 'date price signal')
MissingSignal = namedtuple('MissingSignal', 'date price signal')
