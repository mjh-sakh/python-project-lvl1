#!/usr/bin/env python
"""Empty docstring."""

import prompt


def welcome_user():
    """Asks player's name and greeds."""
    name = prompt.string('May I have your name?\n')
    print(f'{name}! Welcome to the Brain Games!')
