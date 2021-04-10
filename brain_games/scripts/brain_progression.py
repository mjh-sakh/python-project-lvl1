#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game
from brain_games.games import progression


def main():
    """Run progression game."""
    run_game(progression)


if __name__ == '__main__':
    main()
