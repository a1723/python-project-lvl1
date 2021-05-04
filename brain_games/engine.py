import prompt, random
from brain_games.scripts.brain_games import main as welcome_user

name = welcome_user()


def generate_number():
    return random.randint(0, 10)


#Аргументы необязательны для универсальности и использованияя функции во всех играх
def get_user_answer(num1, num2 = '', operation_type = ''):
    return prompt.string(f'Question: {num1} {operation_type} {num2}\nYour answer: ')


def get_wrong_answer(correct_answer, answer):
    print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}\nLet\'s try again, {name}!')

#универсальная функция
def get_congratulations():
    print(f'Congratulations, {name}!')

