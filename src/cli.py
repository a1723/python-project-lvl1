import prompt
from games.brain_even import brain_even
from games.brain_calc import brain_calc
from games.brain_gcd import brain_gcd
from games.brain_prime import brain_prime
from games.brain_progression import brain_progression


def main():
    player_name = entering_player_name()
    game = entering_game_name()
    if not game in('even', 'calc', 'gcd', 'prime', 'progression'):
        print('You typed incorrect game name!')
        return
    elif game == 'even':
        brain_even(player_name)
    elif game == 'calc':
        brain_calc(player_name)
    elif game == 'gcd':
        brain_gcd(player_name)
    elif game == 'prime':
        brain_prime(player_name)
    elif game == 'progression':
        brain_progression(player_name)


def entering_player_name():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def entering_game_name():
    game = prompt.string('Type the name of the game from the list: even, calc, gcd, prime, progression\n')
    print(f'You choose the {game} game!')
    return game


"""GAMES = {
    brain_even(player_name): 'even',
    brain_calc(player_name): 'calc',
    brain_gcd(player_name): 'gcd',
    brain_prime(player_name): 'prime',
    brain_progression(player_name): 'progression'
}


def main():
    player_name = entering_player_name()
    game = entering_game_name()
    if not game in GAMES.values:
        print('You typed incorrect game name!')
    return GAMES[game](player_name)"""
