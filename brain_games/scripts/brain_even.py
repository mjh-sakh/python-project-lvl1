#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_engine import run
from brain_games.games import even


def main():
    """Run guess even number game."""
    run(even)


if __name__ == '__main__':
    main()
