"""First pre-game."""

import prompt


def welcome():
    """Ask name and say hello."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')  # noqa: WPS421
