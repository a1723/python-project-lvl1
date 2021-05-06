#!/usr/bin/env python

import prompt
from brain_games.engine import (
    generate_number,
    get_congratulations,
    check_answer
)


def get_correct_answer(num1, num2):   # проверяем число на чётность
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (str(num1 + num2))


def get_user_answer(num1, num2):
    return prompt.string(f'Question: {num1} {num2}\nYour answer: ')


def main():
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0
    while correct_answers < 3:
        num1 = generate_number()
        num2 = generate_number()
        answer = get_user_answer(num1, num2)
        correct_answer = get_correct_answer(num1, num2)
        correct_answers = check_answer(answer, correct_answer, correct_answers)
    get_congratulations()
