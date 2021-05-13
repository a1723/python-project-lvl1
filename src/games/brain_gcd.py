#!/usr/bin/env python

import prompt
from src.helpers import (
    generate_number,
    get_congratulations,
    check_answer
)
from src.helpers import MAX_ROUNDS


def get_correct_answer(num1, num2):   # проверяем число на чётность
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (str(num1 + num2))


def get_user_answer(num1, num2):
    return prompt.string(f'Question: {num1} {num2}\nYour answer: ')


def brain_gcd(player_name):
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0
    while correct_answers < MAX_ROUNDS:
        num1 = generate_number()
        num2 = generate_number()
        answer = get_user_answer(num1, num2)
        correct_answer = get_correct_answer(num1, num2)
        correct_answers = check_answer(answer, correct_answer, correct_answers, player_name)
    get_congratulations(player_name)
