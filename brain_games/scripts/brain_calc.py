#!/usr/bin/env python
import operator, random
from brain_games.engine import generate_number, get_user_answer, get_wrong_answer, get_congratulations


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_operation_type():
    return random.choice(list(operations.keys()))


def get_correct_answer(operation_type, num1, num2):
    return str(operations[operation_type](num1, num2))


def main():
    print('What is the result of the expression?')

    correct_answers = 0
    while correct_answers < 3:
        num1 = generate_number()
        num2 = generate_number()
        operation_type = get_operation_type()
        correct_answer = get_correct_answer(operation_type, num1, num2)
        answer = get_user_answer(num1, num2, operation_type)

        if (answer == correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            get_wrong_answer(correct_answer, answer)
            return
        
    get_congratulations()


if __name__ == '__main__':
    main()