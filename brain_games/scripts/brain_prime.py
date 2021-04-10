#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game
from brain_games.games import prime


def main():
    """Run prime game."""
    run_game(prime)


if __name__ == '__main__':
    main()
