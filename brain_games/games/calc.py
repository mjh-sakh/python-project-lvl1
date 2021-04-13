# noqa: D100
import random

RULE = 'What is the result of the expression?'


def generate_task_answer():  # noqa: WPS210
    """
    Generate task and answer for cal game.

    Returns:
        task: equation to be calculated, str.
        answer: result of equation, str.
    """
    operators = {
        '+': lambda a, b: a + b,  # noqa: WPS111
        '-': lambda a, b: a - b,  # noqa: WPS111
        '*': lambda a, b: a * b,  # noqa: WPS111
    }
    number1 = random.randint(20, 50)  # noqa: S311, WPS111, WPS432
    number2 = random.randint(1, 20)  # noqa: S311, WPS111, WPS432
    operator = random.choice(list(operators.keys()))  # noqa: S311
    task = f'{number1} {operator} {number2}'
    answer = str(operators[operator](number1, number2))
    return task, answer
