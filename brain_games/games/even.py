# noqa: D100

import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_task_answer():
    """
    Generate task and answer for even number game is even or not.

    Returns:
        task: number to be guessed, str.
        answer: 'yes' for even, 'no' for odd, str.
    """
    task = random.randint(1, 100)  # noqa: S311
    answer = 'yes' if task % 2 == 0 else 'no'
    return str(task), answer
