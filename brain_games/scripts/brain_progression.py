#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game
from brain_games.games import game_progression_engine


def main():
    """Run progression game."""
    run_game(game_progression_engine)


if __name__ == '__main__':
    main()
