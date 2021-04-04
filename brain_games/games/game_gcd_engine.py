# noqa: D100

import random

GAME_GCD_RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(number1: int, number2: int) -> int:
    """
    Find GCD for two numbers.

    Args:
        number1: int
        number2: int

    Returns:
        gcd:
    """
    if number2 > number1:
        return find_gcd(number2, number1)
    if number2 == 0:
        return number1
    return find_gcd(number2, number1 % number2)


def play_game_gcd():
    """
    Generate task and answer for even number game is even or not.

    Returns:
        numbers: str
        correct_answer: str
    """
    number1 = random.randint(1, 100)  # noqa: S311
    number2 = random.randint(1, 100)  # noqa: S311
    correct_answer = str(find_gcd(number1, number2))
    return f'{number1} {number2}', correct_answer  # noqa: WPS305
