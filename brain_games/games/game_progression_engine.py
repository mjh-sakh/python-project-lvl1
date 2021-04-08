# noqa: D100
import random

RULES = 'What number is missing in the progression?'


def logic():
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
    series = [random.randint(40, 70)]  # noqa: S311, WPS432
    for _ in range(random.randint(6, 10)):  # noqa: S311, WPS432
        series.append(series[-1] + increment)
    ix = random.randint(0, len(series) - 1)  # noqa: S311
    lookup_element = series[ix]
    series[ix] = '..'
    progression = ' '.join(map(str, series))
    return progression, str(lookup_element)
