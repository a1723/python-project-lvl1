#!/usr/bin/env python

import prompt
from helpers import (
    generate_number,
    get_congratulations,
    check_answer
)
from helpers import MAX_ROUNDS


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

    rounds = 0
    correct_rounds = 0
    while rounds < MAX_ROUNDS:
        num1 = generate_number()
        num2 = generate_number()
        answer = get_user_answer(num1, num2)
        correct_answer = get_correct_answer(num1, num2)
        correct_rounds = check_answer(answer, correct_answer, rounds, player_name)
        rounds += 1
        if (correct_rounds != rounds):
            return correct_rounds
    return correct_rounds
    get_congratulations(player_name, correct_rounds)

