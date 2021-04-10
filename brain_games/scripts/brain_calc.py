#!/usr/bin/env python
"""Initiate and run Calc game."""

from brain_games.game_core import run_game
from brain_games.games import calc


def main():
    """Run calc game."""
    run_game(calc)


if __name__ == '__main__':
    main()
