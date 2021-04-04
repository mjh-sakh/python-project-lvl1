#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game_engine
from brain_games.cli import welcome_user
from brain_games.games import game_gcd_engine


def main():
    """Run gcd game."""
    name = welcome_user()
    print(game_gcd_engine.GAME_GCD_RULE)  # noqa: WPS421
    run_game_engine(game_gcd_engine.play_game_gcd, name)


if __name__ == '__main__':
    main()
