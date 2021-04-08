#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import initiate_game
from brain_games.games import game_gcd_engine


def main():
    """Run gcd game."""
    initiate_game(
        game_gcd_engine.play_game_gcd,
        game_gcd_engine.GAME_GCD_RULE,
    )


if __name__ == '__main__':
    main()
