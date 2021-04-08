#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import initiate_game
from brain_games.games import game_even_engine


def main():
    """Run guess even number game."""
    initiate_game(
        game_even_engine.play_game_even,
        game_even_engine.GAME_EVEN_RULE,
    )


if __name__ == '__main__':
    main()
