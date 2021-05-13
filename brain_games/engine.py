import prompt
import random
from brain_games.cli import main as entering_user_name

user_name = entering_user_name()
wrong_answer = ' is wrong answer ;(. Correct answer was '


def generate_number():
    return random.randint(2, 30)


def generate_progression():
    step = random.randint(1, 5)
    progression = []
    for i in range(1, 100, step):
        progression.append(i)
    return progression


# Аргументы необязательны для универсальности и использованияя
# функции во всех играх кроме brain_gcd (из-за ненадобности пробела)

def get_user_answer(num1, num2='', operation=''):
    return prompt.string(f'Question: {num1} {operation} {num2}\nYour answer: ')


def check_answer(answer, correct_answer, count_correct_answers):
    if (answer == correct_answer):
        print('Correct!')
        count_correct_answers += 1
        return count_correct_answers
    else:
        get_wrong_answer(correct_answer, answer)


def get_wrong_answer(correct_answer, answer):
    print(f'{answer}{wrong_answer}{correct_answer}\nLet\'s try again, {user_name}!')
    exit()


def get_congratulations():
    print(f'Congratulations, {user_name}!')

