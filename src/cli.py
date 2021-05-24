import prompt
from games.brain_even import brain_even
from games.brain_calc import brain_calc
from games.brain_gcd import brain_gcd
from games.brain_prime import brain_prime
from games.brain_progression import brain_progression
from base import inserting_into_db


GAMES = {
    'even': brain_even,
    'calc': brain_calc,
    'gcd': brain_gcd,
    'prime': brain_prime,
    'progression': brain_progression
}


def main():
    player_name = entering_player_name()
    game = entering_game_name()
    if not game in GAMES.keys():
        print('You typed incorrect game name!')
    result = GAMES[game](player_name)
    inserting_into_db(player_name, game, result)


def entering_player_name():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def entering_game_name():
    game = prompt.string('Type the name of the game from the list: even, calc, gcd, prime, progression\n')
    print(f'You choose the {game} game!')
    return game
