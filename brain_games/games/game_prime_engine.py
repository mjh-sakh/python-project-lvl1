# noqa: D100
import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


def is_prime(number: int) -> bool:
    """
    Check whether given number is prime.

    Args:
        number: int

    Returns:
        bool:
    """
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    sqr = int(number**0.5) + 1

    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True


def task_answer_generator():
    """
    Generate task and answer for prime game.

    Returns:
        number: str.
        correct_answer: str.
    """
    number = random.randint(11, 99)  # noqa: S311, WPS432
    return str(number), 'yes' if is_prime(number) else 'no'
