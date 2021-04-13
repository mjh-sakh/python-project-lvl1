# noqa: D100
import random

RULE = 'What number is missing in the progression?'


def generate_progression(initial_value, increment, progression_length):
    """
    Generate and returns progression list.

    Args:
        initial_value: int
        increment: int
        progression_length: int

    Returns:
         progression: list
    """
    return list(map(lambda x: initial_value + x * increment, range(progression_length)))  # noqa: WPS221, WPS111, E501


def generate_task_answer():  # noqa: WPS210
    """
    Generate task and answer for progression game.

    Returns:
        task: progression, str
        answer: lookup element, str.
    """
    while True:
        increment = random.randint(-11, 11)  # noqa: S311, WPS432
        if increment != 0:
            break
    initial_value = random.randint(40, 70)  # noqa: S311, WPS432
    progression_length = random.randint(6, 10)  # noqa: S311, WPS432
    progression = generate_progression(initial_value, increment, progression_length)  # noqa: WPS221, WPS111, E501
    lookup_element_ix = random.randint(0, len(progression) - 1)  # noqa: S311
    lookup_element = progression[lookup_element_ix]
    progression[lookup_element_ix] = '..'
    progression_string = ' '.join(map(str, progression))
    return progression_string, str(lookup_element)
