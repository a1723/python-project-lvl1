#!/usr/bin/env python

from brain_games.engine import prompt, randint, name, generate_number



def check_number_for_parity(number):   #проверяем число на чётность
    if (number % 2 == 0): 
        return "yes"
    else:
        return "no"


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = generate_number()
        answer = prompt.string('Question: {0}{1}Your answer: '.format(number, '\n'))
        if ((number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no')):
            print('Correct!')
            correct_answers += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'{2}Let\'s try again, {3}!".format(answer, check_number_for_parity(number), '\n',  name))
            return
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()

