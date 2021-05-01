#!/usr/bin/env python

import prompt
from random import randint
from brain_games.cli import entering_user_name.name
from brain_games.scripts.brain_games import main as welcome_user




def check_number(number):
    if (number % 2 == 0): 
        return 'yes'
    else:
        return 'no'


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = randint(0, 100)
        Question = prompt.string('Question: ' + str(number) + '\n')
        print('Your answer: ' + Question)
        if ((number % 2 == 0 and Question == 'yes') or (number % 2 != 0 and Question == 'no')):
            print('Correct!')
            correct_answers += 1
        else:
            print(Question + ' ' + 'is wrong answer ;(. Correct answer was' + ' ' + check_number(number) + '\n' + 'Let\'s try again, ' + entering_user_name.name + '!')
            return
    print ('Congratulations, ' + entering_user_name.name + '!')


if __name__ == '__main__':
    main()
