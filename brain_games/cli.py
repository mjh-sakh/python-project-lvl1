# noqa: D100

import prompt


def just_say_hello():
    """Ask name and say hello."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')  # noqa: WPS421, WPS305


def ask_player_name():
    """
    Ask player's name and greed.

    Returns:
        name: Name of player.

    :return Name of player.
    """
    name = prompt.string('May I have your name?\n')
    return name


def welcome_player(name):
    """
    Welcome player by name.

    Args:
        name: str
    """
    print(f'{name}! Welcome to the Brain Games!')  # noqa: WPS421, WPS305
