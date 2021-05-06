
from brain_games.engine import (
    generate_number,
    get_user_answer,
    get_congratulations,
    check_answer
)


def get_correct_answer(num1):   # проверяем число на чётность
    return "yes" if (num1 % 2 == 0) else "no"


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        num1 = generate_number()
        answer = get_user_answer(num1)
        correct_answer = get_correct_answer(num1)
        correct_answers = check_answer(answer, correct_answer, correct_answers)
    get_congratulations()
