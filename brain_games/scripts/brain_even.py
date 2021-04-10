#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game
from brain_games.games import even


def main():
    """Run guess even number game."""
    run_game(even)


if __name__ == '__main__':
    main()
