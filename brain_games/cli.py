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
    counter_correct_answers = 0
    while True:
        number = random.randint(1, 100)  # noqa: S311
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')  # noqa: WPS421, WPS305
        if prompt.string('Your answer: ') == correct_answer:
            counter_correct_answers += 1
            print('Correct!')  # noqa: WPS421
        else:
            print(f"Let's try again, {name}!")  # noqa: WPS421, WPS305
            break
        if counter_correct_answers == 3:
            print(f'Congratulations, {name}!')  # noqa: WPS421, WPS305
            break
