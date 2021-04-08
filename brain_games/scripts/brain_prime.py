#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game
from brain_games.games import game_prime_engine


def main():
    """Run prime game."""
    run_game(game_prime_engine)


if __name__ == '__main__':
    main()
