"""Functions that request data input from player."""

import prompt


def just_say_hello():
    """Ask name and say hello."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')  # noqa: WPS421, WPS305


def ask_player_name():
    """
    Ask player's name.

    Returns:
        name: Name of player.
    """
    return prompt.string('May I have your name?\n')


def ask_answer_from_player():
    """
    Ask player's answer.

    Returns:
        answer: str.
    """
    return prompt.string('Your answer: ')
