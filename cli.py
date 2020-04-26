"""Main function for `sigalgo`."""


import operator

from zca.pipelines.zscore import ZScorePipeline
from zca.parsers import CSVParser
from zca.records.streams import RecordStream


def sort_on_timestamp(data):
    """Sort on the 1st item of a `record`: timestamp."""
    return sorted(data, key=operator.itemgetter(0))


def check_file_data(file_path: str):
    """"Checks the csv provided by `file_path` and finds:

        1. Missing Data
        2. Stale data (7 days unchanged)
        3. Outliers

    NOTE: lag and threshold probably need some kind of hyperparametrization,
          or some `influence` mechanism - especially with non-stationary data
    """
    parser = CSVParser(file_path)
    rec_stream = RecordStream(parser)  # data formatter
    record_formatted_data_gen = rec_stream.parse()
    pipeline = ZScorePipeline(lag=15, threshold=3)  # algo pipeline
    signals = pipeline.pipe(sort_on_timestamp(list(record_formatted_data_gen)))

    return signals


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    to_check = check_file_data(path)

    if to_check:
        for rec in to_check:
            print(rec)

        print("FOUND: ", len(to_check), "anomalies")

    else:
        print("Data is completely clean")
