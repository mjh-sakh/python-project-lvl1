# noqa: D100

from brain_games.cli import get_input_from_player, show_message

REQUIRED_WIN_COUNT = 3


def run_game(game_engine):
    """
    Rung game using provided engine.

    First, welcome user, print rules, start game engine.

    Args:
        game_engine: package
    """
    name = get_input_from_player('May I have your name?\n')
    show_message(f'{name}! Welcome to the Brain Games!')  # noqa: WPS305
    show_message(game_engine.RULES)
    counter_correct_answers = 0
    while counter_correct_answers < REQUIRED_WIN_COUNT:
        task, correct_answer = game_engine.generate_task_answer()
        show_message(f'Question: {task}')  # noqa: WPS305
        answer = get_input_from_player('Your answer: ')
        if answer == correct_answer:
            counter_correct_answers += 1
            show_message('Correct!')
        else:
            show_message(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: WPS305, E501
            show_message(f"Let's try again, {name}!")  # noqa: WPS305
            break
    else:
        show_message(f'Congratulations, {name}!')  # noqa: WPS305


def say_hello():
    """Ask name and say hello."""
    name = get_input_from_player('May I have your name? ')
    show_message(f'Hello, {name}!')  # noqa: WPS305