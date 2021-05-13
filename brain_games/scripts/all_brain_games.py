from brain_games.cli import entering_game_name
from brain_games.games.brain_even import main as brain_even
from brain_games.games.brain_calc import main as brain_calc
from brain_games.games.brain_gcd import main as brain_gcd
from brain_games.games.brain_prime import main as brain_prime
from brain_games.games.brain_progression import main as brain_progression


def main():
    game = entering_game_name()
    if not game in('even', 'calc', 'gcd', 'prime', 'progression'):
        print('You typed incorrect game name!')
        return
    elif game == 'even':
        brain_even()
    elif game == 'calc':
        brain_calc()
    elif game == 'gcd':
        brain_gcd()
    elif game == 'prime':
        brain_prime()
    elif game == 'progression':
        brain_progression()
    return game

