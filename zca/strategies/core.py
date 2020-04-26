"""Core base classes for the strategy module."""


import abc


class BaseStrategy(metaclass=abc.ABCMeta):
    """Abstract class: defines the strategy `interface` and `type`.
    """
    @abc.abstractmethod
    def process(self, data):
        """Abstract `process` mehthod: Override with strategy application."""
