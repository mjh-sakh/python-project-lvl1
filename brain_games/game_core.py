# noqa: D100
import prompt
from brain_games.cli import ask_player_name, welcome_player

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
    run_game_logic_for_player(game_engine.logic, name)


def run_game_logic_for_player(game_logic, name):
    """
    Start game play.

    Args:
        game_logic: function that returns str, str
        name: players name
    """
    counter_correct_answers = 0
    while counter_correct_answers < REQUIRED_WIN_COUNT:
        task, correct_answer = game_logic()
        print(f'Question: {task}')  # noqa: WPS421, WPS305
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            counter_correct_answers += 1
            print('Correct!')  # noqa: WPS421
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: WPS421, WPS305, E501
            print(f"Let's try again, {name}!")  # noqa: WPS421, WPS305
            break
    else:
        print(f'Congratulations, {name}!')  # noqa: WPS421, WPS305
