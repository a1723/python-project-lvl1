#!/usr/bin/env python

import collections as coll
from helpers import (
    generate_number,
    get_user_answer,
    get_congratulations,
    check_answer
)
from helpers import MAX_ROUNDS


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


def brain_prime(player_name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    rounds = 0
    correct_rounds = 0
    while rounds < MAX_ROUNDS:
        num = generate_number()
        result_values = get_number_divisors(num)
        correct_answer = get_correct_answer(result_values, num)
        answer = get_user_answer(num)
        correct_rounds = check_answer(answer, correct_answer, rounds, player_name)
        rounds += 1
        if (correct_rounds != rounds):
            return correct_rounds
    return correct_rounds
    get_congratulations(player_name, correct_rounds)
