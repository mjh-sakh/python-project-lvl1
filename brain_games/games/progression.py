# noqa: D100
import random

RULES = 'What number is missing in the progression?'


def generate_task_answer():  # noqa: WPS210
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
    series = list(map(lambda x: initial_value + x * increment, range(series_length - 1)))  # noqa: WPS221, WPS111, E501
    lookup_element_ix = random.randint(0, len(series))  # noqa: S311
    lookup_element = series[lookup_element_ix]
    series[lookup_element_ix] = '..'
    progression = ' '.join(map(str, series))
    return progression, str(lookup_element)
