#!/usr/bin/env python
"""Initiate and run Even game."""

from brain_games.game_engine import run
from brain_games.games import prime


def main():
    """Run prime game."""
    run(prime)


if __name__ == '__main__':
    main()
