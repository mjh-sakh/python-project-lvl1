#!/usr/bin/env python
"""Initiate and run Calc game."""

from brain_games.game_engine import run
from brain_games.games import calc


def main():
    """Run calc game."""
    run(calc)


if __name__ == '__main__':
    main()
