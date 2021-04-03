"""Empty docstring."""

import random
import prompt


def welcome_user():
    """
    Ask player's name and greed.

    Returns:
        name: Name of player.

    :return Name of player.
    """
    name = prompt.string('May I have your name?\n')
    print(f'{name}! Welcome to the Brain Games!')  # noqa: WPS421, WPS305
    return name


def play_game_even_check(name):
    """
    Start simple game to say if number is even or not.

    Args:
        name: Player name.
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')  # noqa: WPS421, E501
    while True:
        number = random.randint(1, 100)  # noqa: S311
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')  # noqa: WPS421, WPS305
        if prompt.string('Your answer: ') == correct_answer:
            print('Correct!')  # noqa: WPS421
        else:
            break
    print(f"Let's try again, {name}!")  # noqa: WPS421, WPS305
