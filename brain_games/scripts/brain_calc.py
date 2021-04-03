#!/usr/bin/env python
"""Initiate and run Calc game."""

from brain_games.cli import Game
from brain_games.games import game_calc_engine


def main():
    """Run guess even number game."""
    game = Game(game_calc_engine.play_game_calc, game_calc_engine.GAME_CALC_RULE)  # noqa: E501
    game.run()


if __name__ == '__main__':
    main()
