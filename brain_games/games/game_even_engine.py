# noqa: D100

import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic():
    """
    Generate task and answer for even number game is even or not.

    Returns:
        number: number to be guessed.
        correct_answer: 'yes' for even, 'no' for odd.
    """
    number_for_question = random.randint(1, 100)  # noqa: S311
    correct_answer = 'yes' if number_for_question % 2 == 0 else 'no'
    return number_for_question, correct_answer
