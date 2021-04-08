#!/usr/bin/env python
"""Initiate and run Calc game."""

from brain_games.game_core import run_game
from brain_games.games import game_calc_engine


def main():
    """Run calc game."""
    run_game(game_calc_engine)


if __name__ == '__main__':
    main()
