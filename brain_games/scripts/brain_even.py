#!/usr/bin/env python

from brain_games.engine import prompt, name, generate_number, get_user_answer, get_wrong_answer, get_congratulations


def get_correct_answer(num1):   #проверяем число на чётность
    return "yes" if (num1 % 2 == 0) else "no"
    

def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        num1 = generate_number()
        answer = get_user_answer(num1)
        correct_answer = get_correct_answer(num1)
        if (answer == correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            get_wrong_answer(correct_answer, answer)
            return

    get_congratulations()


if __name__ == '__main__':
    main()

