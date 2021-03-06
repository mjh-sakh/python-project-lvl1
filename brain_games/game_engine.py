# noqa: D100

from brain_games.user_interface import get_input_from_player, show_message

REQUIRED_WINS_COUNT = 3


def run(game):
    """
    Rung game using provided engine.

    First, welcome user, print rules, start game engine.

    Args:
        game: package
    """
    name = get_input_from_player('May I have your name?\n')
    show_message(f'{name}! Welcome to the Brain Games!')
    show_message(game.RULE)
    counter_correct_answers = 0
    while counter_correct_answers < REQUIRED_WINS_COUNT:
        task, correct_answer = game.generate_task_answer()
        show_message(f'Question: {task}')
        answer = get_input_from_player('Your answer: ')
        if answer == correct_answer:
            counter_correct_answers += 1
            show_message('Correct!')
        else:
            show_message(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            show_message(f"Let's try again, {name}!")
            break
    else:
        show_message(f'Congratulations, {name}!')
