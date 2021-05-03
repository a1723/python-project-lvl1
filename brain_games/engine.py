import prompt
from random import choice, randint
from brain_games.scripts.brain_games import main as welcome_user

name = welcome_user()

def generate_number():
    return randint(0, 10)


def summa(a ,b):
    summa = a + b
    return str(summa)


def difference(a ,b):
    diff = a - b
    return str(diff)


def multiplication(a ,b):
    multi = a * b
    return str(multi)


# functions for calc task
funcs = (summa, difference, multiplication)

