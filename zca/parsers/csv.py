"""CSV Parser."""


class CSVParser:
    """CSV parser class."""
    def __init__(self, filepath: str, method='r', headers=True):
        self._filepath = filepath
        self._method = method
        self._headers = headers

    def __iter__(self):
        """Provides Iterable protocol."""
        with open(self._filepath) as f:
            if self._headers:
                next(f)

            stream = iter(f.readline, '')
            yield from stream
