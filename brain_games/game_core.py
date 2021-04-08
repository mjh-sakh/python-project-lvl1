# noqa: D100
import prompt
from brain_games.cli import welcome_user

REQUIRED_WIN_COUNT = 3


def initiate_game(game_engine, rules):
    """
    Initiate game. Welcome user, print rules, start game engine.

    Args:
        game_engine: func
        rules: str
    """
    name = welcome_user()
    print(rules)  # noqa: WPS421
    run_game_engine(game_engine, name)


def run_game_engine(game_engine, name):
    """
    Start game play.

    Args:
        game_engine: function that returns str, str
        name: players name
    """
    counter_correct_answers = 0
    while True:
        task, correct_answer = game_engine()
        print(f'Question: {task}')  # noqa: WPS421, WPS305
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            counter_correct_answers += 1
            print('Correct!')  # noqa: WPS421
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: WPS421, WPS305, E501
            print(f"Let's try again, {name}!")  # noqa: WPS421, WPS305
            break
        if counter_correct_answers == REQUIRED_WIN_COUNT:
            print(f'Congratulations, {name}!')  # noqa: WPS421, WPS305
            break
