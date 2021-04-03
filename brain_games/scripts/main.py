#!/usr/bin/env python
"""Empty docstring."""

from brain_games import cli


def main():
    """Game run."""
    name = cli.welcome_user()
    cli.play_game_even_check(name)


if __name__ == '__main__':
    main()
