
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

    rounds = 0
    correct_rounds = 0
    while rounds < MAX_ROUNDS:
        num1 = generate_number()
        answer = get_user_answer(num1)
        correct_answer = get_correct_answer(num1)
        correct_rounds = check_answer(answer, correct_answer, rounds, player_name)
        rounds += 1
        if (correct_rounds != rounds):
            return correct_rounds
    return correct_rounds
    get_congratulations(player_name, correct_rounds)
