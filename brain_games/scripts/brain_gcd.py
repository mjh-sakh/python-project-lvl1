#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_engine import run
from brain_games.games import gcd


def main():
    """Run gcd game."""
    run(gcd)


if __name__ == '__main__':
    main()
