# noqa: D100
import random

RULES = 'What is the result of the expression?'


def task_answer_generator():
    """
    Generate task and answer for cal game.

    Returns:
        equation: to be calculated.
        correct_answer: correct result.
    """
    operators = {
        '+': lambda a, b: a + b,  # noqa: WPS111
        '-': lambda a, b: a - b,  # noqa: WPS111
        '*': lambda a, b: a * b,  # noqa: WPS111
    }
    a = random.randint(20, 50)  # noqa: S311, WPS111, WPS432
    b = random.randint(1, 20)  # noqa: S311, WPS111, WPS432
    operator = random.choice(list(operators.keys()))  # noqa: S311
    equation = ' '.join([str(a), operator, str(b)])
    return equation, str(operators[operator](a, b))
