import prompt, random
from brain_games.scripts.brain_games import main as welcome_user

name = welcome_user()


def generate_number():
    return random.randint(1, 10)


#Аргументы необязательны для универсальности и использованияя функции во всех играх
def get_user_answer(num1, num2 = '', operation_type = ''):
    return prompt.string(f'Question: {num1} {operation_type} {num2}\nYour answer: ')


def check_answer(answer, correct_answer, count_correct_answers):
    if (answer == correct_answer):
        print('Correct!')
        count_correct_answers += 1
        return count_correct_answers
    else:
        get_wrong_answer(correct_answer, answer)


def get_wrong_answer(correct_answer, answer):
    print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}\nLet\'s try again, {name}!')
    exit()

def get_congratulations():
    print(f'Congratulations, {name}!')

