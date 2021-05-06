#!/usr/bin/env python

import collections as coll
from brain_games.engine import (
    generate_number,
    get_user_answer,
    get_congratulations,
    check_answer
)


def get_number_divisors(num):
    i = 1
    result_values = []
    while (num >= i):
        if (num % i == 0):
            result_values.append(i)
        i += 1
    return result_values


def get_correct_answer(result_values, num):
    correct_values = [1, num]
    if (coll.Counter(result_values) == coll.Counter(correct_values)):
        return "yes"
    return "no"


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        num = generate_number()
        result_values = get_number_divisors(num)
        correct_answer = get_correct_answer(result_values, num)
        answer = get_user_answer(num)
        correct_answers = check_answer(answer, correct_answer, correct_answers)
    get_congratulations()
