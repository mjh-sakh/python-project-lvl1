# noqa: D100

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
