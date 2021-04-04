#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game_engine
from brain_games.cli import welcome_user
from brain_games.games import game_even_engine


def main():
    """Run guess even number game."""
    name = welcome_user()
    print(game_even_engine.GAME_EVEN_RULE)  # noqa: WPS421
    run_game_engine(game_even_engine.play_game_even, name)


if __name__ == '__main__':
    main()
