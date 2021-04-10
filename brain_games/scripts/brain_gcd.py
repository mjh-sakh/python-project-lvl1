#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game
from brain_games.games import gcd


def main():
    """Run gcd game."""
    run_game(gcd)


if __name__ == '__main__':
    main()
