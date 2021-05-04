#!/usr/bin/env python

from brain_games.engine import generate_number, get_user_answer, get_congratulations, check_answer

def get_correct_answer(num1, num2):   #проверяем число на чётность
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (str(num1 + num2))


def main():
    print('Find the greatest common divisor of given numbers.')

    count_correct_answers = 0
    while count_correct_answers < 3:
        num1 = generate_number()
        num2 = generate_number()
        answer = get_user_answer(num1, num2)
        correct_answer = get_correct_answer(num1, num2)
        count_correct_answers = check_answer(answer, correct_answer, count_correct_answers)
    get_congratulations()


if __name__ == '__main__':
    main()
