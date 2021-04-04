#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game_engine
from brain_games.cli import welcome_user
from brain_games.games import game_progression_engine


def main():
    """Run progression game."""
    name = welcome_user()
    print(game_progression_engine.GAME_PROGRESSION_RULE)  # noqa: WPS421
    run_game_engine(game_progression_engine.play_game_progression, name)


if __name__ == '__main__':
    main()
