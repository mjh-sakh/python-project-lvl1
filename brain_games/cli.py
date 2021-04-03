"""Empty docstring."""

import prompt


def welcome_user():
    """
    Ask player's name and greed.

    Returns:
        name: Name of player.

    :return Name of player.
    """
    name = prompt.string('May I have your name?\n')
    print(f'{name}! Welcome to the Brain Games!')  # noqa: WPS421, WPS305
    return name


class Game(object):
    """Connect games logic with specific game engine."""

    def __init__(self, game_engine, rule):
        """
        Initiate game.

        Args:
            game_engine: function -> str, str
            rule: string

        """
        self.game_engine = game_engine
        self.name = welcome_user()
        self.rule = rule
        self.win_count = 3

    def print_rule(self):
        """Print rule for game."""
        print(self.rule)  # noqa: WPS421

    def run(self):
        """Start game."""
        counter_correct_answers = 0
        while True:
            task, correct_answer = self.game_engine()
            print(f'Question: {task}')  # noqa: WPS421, WPS305
            answer = prompt.string('Your answer: ')
            if answer == correct_answer:
                counter_correct_answers += 1
                print('Correct!')  # noqa: WPS421
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: WPS421, WPS305, E501
                print(f"Let's try again, {self.name}!")  # noqa: WPS421, WPS305
                break
            if counter_correct_answers == self.win_count:
                print(f'Congratulations, {self.name}!')  # noqa: WPS421, WPS305
                break
