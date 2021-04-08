# noqa: D100

import random

RULES = 'Find the greatest common divisor of given numbers.'


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


def logic():
    """
    Generate task and answer for gcd game.

    Returns:
        numbers: str
        correct_answer: str
    """
    initial_gcd = random.randint(2, 9)  # noqa: S311
    number1 = random.randint(2, 5) * initial_gcd  # noqa: S311
    number2 = random.randint(4, 9) * initial_gcd  # noqa: S311
    correct_answer = str(find_gcd(number1, number2))
    return f'{number1} {number2}', correct_answer  # noqa: WPS305
