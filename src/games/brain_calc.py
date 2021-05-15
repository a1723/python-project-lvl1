#!/usr/bin/env python

import operator
import random
from helpers import (
    generate_number,
    get_user_answer,
    get_congratulations,
    check_answer
)
from helpers import MAX_ROUNDS


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_operation_type():
    return random.choice(list(operations.keys()))


def get_correct_answer(operation_type, num1, num2):
    return str(operations[operation_type](num1, num2))


def brain_calc(player_name):
    print('What is the result of the expression?')

    correct_answers = 0
    while correct_answers < MAX_ROUNDS:
        num1 = generate_number()
        num2 = generate_number()
        operation_type = get_operation_type()
        correct_answer = get_correct_answer(operation_type, num1, num2)
        answer = get_user_answer(num1, num2, operation_type)
        correct_answers = check_answer(answer, correct_answer, correct_answers, player_name)
    get_congratulations(player_name)
