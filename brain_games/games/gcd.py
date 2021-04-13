# noqa: D100

import random

RULE = 'Find the greatest common divisor of given numbers.'


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


def generate_task_answer():
    """
    Generate task and answer for gcd game.

    Returns:
        task: two numbers, str.
        answer: str
    """
    initial_gcd = random.randint(2, 9)  # noqa: S311
    number1 = random.randint(2, 5) * initial_gcd  # noqa: S311
    number2 = random.randint(4, 9) * initial_gcd  # noqa: S311
    task = f'{number1} {number2}'
    answer = str(find_gcd(number1, number2))
    return task, answer
