import prompt


def main():
    print('Welcome to the Brain Games!')
    welcome = prompt.string('May I have your name? ')
    print(f'Hello, {welcome}!')
    return welcome


def entering_game_name():
    game = prompt.string('Type the name of the game from the list: even, calc, gcd, prime, progression\n')
    print(f'You choose the {game} game!')
    return game

