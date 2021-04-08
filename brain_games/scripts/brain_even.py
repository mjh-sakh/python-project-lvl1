#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game
from brain_games.games import game_even_engine


def main():
    """Run guess even number game."""
    run_game(game_even_engine)


if __name__ == '__main__':
    main()
