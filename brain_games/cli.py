"""Functions that work with CLI."""

import prompt


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


def show_message(message):
    """
    Display given message to users.

    Currently it uses print to cli.

    Args:
        message: str
    """
    print(message)  # noqa: WPS421
