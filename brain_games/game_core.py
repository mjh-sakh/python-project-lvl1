# noqa: D100
from brain_games.cli import ask_answer_from_player, ask_player_name

REQUIRED_WIN_COUNT = 3


def run_game(game_engine):
    """
    Rung game using provided engine.

    First, welcome user, print rules, start game engine.

    Args:
        game_engine: package
    """
    name = ask_player_name()
    show_message(f'{name}! Welcome to the Brain Games!')
    show_message(game_engine.RULES)
    generate_tasks_for_player(game_engine.task_answer_generator, name)


def generate_tasks_for_player(task_answer_generator, name):
    """
    Start game play.

    Args:
        task_answer_generator: function that returns str, str
        name: players name
    """
    counter_correct_answers = 0
    while counter_correct_answers < REQUIRED_WIN_COUNT:
        task, correct_answer = task_answer_generator()
        show_message(f'Question: {task}')  # noqa: WPS305
        answer = ask_answer_from_player()
        if answer == correct_answer:
            counter_correct_answers += 1
            show_message('Correct!')
        else:
            show_message(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: WPS305, E501
            show_message(f"Let's try again, {name}!")  # noqa: WPS305
            break
    else:
        show_message(f'Congratulations, {name}!')  # noqa: WPS305


def show_message(message):
    """
    Display given message to users.

    Currently it uses print to cli.

    Args:
        message: str
    """
    print(message)  # noqa: WPS421
