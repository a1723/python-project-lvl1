
from helpers import (
    generate_number,
    get_user_answer,
    get_congratulations,
    check_answer
)
from helpers import MAX_ROUNDS


def get_correct_answer(num1):   # проверяем число на чётность
    return "yes" if (num1 % 2 == 0) else "no"


def brain_even(player_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < MAX_ROUNDS:
        num1 = generate_number()
        answer = get_user_answer(num1)
        correct_answer = get_correct_answer(num1)
        correct_answers = check_answer(answer, correct_answer, correct_answers, player_name)
    get_congratulations(player_name)
