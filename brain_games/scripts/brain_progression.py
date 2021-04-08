#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import initiate_game
from brain_games.games import game_progression_engine


def main():
    """Run progression game."""
    initiate_game(
        game_progression_engine.game_progression_engine,
        game_progression_engine.GAME_PROGRESSION_RULE,
    )


if __name__ == '__main__':
    main()
