"""Exceptions for the `structures` module."""


class MovingWindowFullError(Exception):
    """Exception for moving window at full capacity.
    """
    pass


class MovingWindowInitializationError(Exception):
    """Exception for initialization Errors.
    """
    pass
