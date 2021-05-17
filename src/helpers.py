import prompt
import random


WRONG_ANSWER = ' is wrong answer ;(. Correct answer was '
MAX_ROUNDS = 3

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


def check_answer(answer, correct_answer, count_correct_answers, player_name):
    if (answer == correct_answer):
        print('Correct!')
        count_correct_answers += 1
        #print(count_correct_answers)
        return count_correct_answers
    else:
        get_wrong_answer(answer, correct_answer, player_name, count_correct_answers)
        return count_correct_answers
    exit()



def get_wrong_answer(answer, correct_answer, player_name, count_correct_answers):
    print(f'{answer}{WRONG_ANSWER}{correct_answer}\nLet\'s try again, {player_name}!')
    #print(count_correct_answers)
    #return count_correct_answers


def get_congratulations(player_name, count_correct_answers):
    print(f'Congratulations, {player_name}!')
    return count_correct_answers