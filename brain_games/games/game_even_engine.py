# noqa: D100

import random

GAME_EVEN_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game_even():
    """
    Generate task and answer for even number game is even or not.

    Returns:
        number: number to be guessed.
        correct_answer: 'yes' for even, 'no' for odd.
    """
    number = random.randint(1, 100)  # noqa: S311
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer
