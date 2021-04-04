#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_core import run_game_engine
from brain_games.cli import welcome_user
from brain_games.games import game_prime_engine


def main():
    """Run prime game."""
    name = welcome_user()
    print(game_prime_engine.GAME_PRIME_RULE)  # noqa: WPS421
    run_game_engine(game_prime_engine.play_game_prime, name)


if __name__ == '__main__':
    main()
