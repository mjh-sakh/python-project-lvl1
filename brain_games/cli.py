"""Functions that request data input from player."""

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
