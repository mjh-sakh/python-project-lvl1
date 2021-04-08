"""Functions that request data input from player."""

import prompt


def just_say_hello():
    """Ask name and say hello."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')  # noqa: WPS421, WPS305


def get_input_from_player(text):
    """
    Ask input from player.

    Show provided text.

    Args:
        text: str.

    Returns:
        input: str.
    """
    return prompt.string(text)
