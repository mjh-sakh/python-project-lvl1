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
    welcome_player(name)
    print(game_engine.RULES)  # noqa: WPS421
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
        print(f'Question: {task}')  # noqa: WPS421, WPS305
        answer = ask_answer_from_player()
        if answer == correct_answer:
            counter_correct_answers += 1
            print('Correct!')  # noqa: WPS421
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: WPS421, WPS305, E501
            print(f"Let's try again, {name}!")  # noqa: WPS421, WPS305
            break
    else:
        print(f'Congratulations, {name}!')  # noqa: WPS421, WPS305


def welcome_player(name):
    """
    Welcome player by name.

    Args:
        name: str
    """
    print(f'{name}! Welcome to the Brain Games!')  # noqa: WPS421, WPS305
