#!/usr/bin/env python

import prompt
from random import randint
from brain_games.cli import entering_user_name
from brain_games.scripts.brain_games import main as welcome_user


def check_number(number):
    if (number % 2 == 0): 
        return "yes"
    else:
        return "no"


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = randint(0, 100)
        Answer = prompt.string('Question: {} '.format(number))
        print('Your answer: {}'.format(Answer))
        if ((number % 2 == 0 and Answer == 'yes') or (number % 2 != 0 and Answer == 'no')):
            print('Correct!')
            correct_answers += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'{2}Let\'s try again, {3}!".format(Answer, check_number(number), '\n',  name))
            return
    print ('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()

