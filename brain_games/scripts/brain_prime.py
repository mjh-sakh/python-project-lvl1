#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import initiate_game
from brain_games.games import game_prime_engine


def main():
    """Run prime game."""
    initiate_game(
        game_prime_engine.game_prime_engine,
        game_prime_engine.GAME_PRIME_RULE,
    )


if __name__ == '__main__':
    main()
