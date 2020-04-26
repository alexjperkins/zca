"""Stats functions."""


def zscore(value, mean, stdev):
    """Calculates the zscore with the following formula:

    Formula:
        z = (value - mean) / stdev
    """
    if stdev == 0:
        # Zero Div Error check
        return 0

    return (value - mean) / stdev
