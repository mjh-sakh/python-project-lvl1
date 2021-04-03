#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.cli import Game
from brain_games.games import game_even_engine


def main():
    """Run guess even number game."""
    game = Game(game_even_engine.play_game_even, game_even_engine.GAME_EVEN_RULE)  # noqa: E501
    game.run()


if __name__ == '__main__':
    main()
