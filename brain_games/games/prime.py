# noqa: D100
import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


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


def generate_task_answer():
    """
    Generate task and answer for prime game.

    Returns:
        number: str.
        answer: yes or no, str.
    """
    number = random.randint(11, 99)  # noqa: WPS432
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer
