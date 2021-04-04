#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.cli import Game
from brain_games.games import game_prime_engine


def main():
    """Run guess even number game."""
    game = Game(game_prime_engine.play_game_prime, game_prime_engine.GAME_PRIME_RULE)  # noqa: E501
    game.run()


if __name__ == '__main__':
    main()
