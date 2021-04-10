# noqa: D100
import random

RULES = 'What number is missing in the progression?'


def populate_series(series, initial_value: int, increment: int, length: int = 10):  # noqa: E501
    """
    Populate given series in place with values starting from initial value.

    Args:
        series: list
        initial_value: int
        increment: int
        length: int

    """
    series.append(initial_value)
    for _ in range(length - 1):
        series.append(series[-1] + increment)


def task_answer_generator():  # noqa: WPS210
    """
    Generate task and answer for progression game.

    Returns:
        progression: str.
        lookup_element: str.
    """
    while True:
        increment = random.randint(-11, 11)  # noqa: S311, WPS432
        if increment != 0:
            break
    initial_value = random.randint(40, 70)  # noqa: S311, WPS432
    series_length = random.randint(6, 10)  # noqa: S311, WPS432
    series = []
    populate_series(series, initial_value, increment, series_length)
    ix = random.randint(0, len(series) - 1)  # noqa: S311
    lookup_element = series[ix]
    series[ix] = '..'
    progression = ' '.join(map(str, series))
    return progression, str(lookup_element)
