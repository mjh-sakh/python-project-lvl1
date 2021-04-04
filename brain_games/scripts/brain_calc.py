#!/usr/bin/env python
"""Initiate and run Calc game."""

from brain_games.game_core import run_game_engine
from brain_games.cli import welcome_user
from brain_games.games import game_calc_engine


def main():
    """Run calc game."""
    name = welcome_user()
    print(game_calc_engine.GAME_CALC_RULE)  # noqa: WPS421
    run_game_engine(game_calc_engine.play_game_calc, name)


if __name__ == '__main__':
    main()
