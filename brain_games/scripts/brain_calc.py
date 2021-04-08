#!/usr/bin/env python
"""Initiate and run Calc game."""

from brain_games.game_core import initiate_game
from brain_games.games import game_calc_engine


def main():
    """Run calc game."""
    initiate_game(
        game_calc_engine.play_game_calc,
        game_calc_engine.GAME_CALC_RULE,
    )


if __name__ == '__main__':
    main()
