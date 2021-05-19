#!/usr/bin/env python

from random import randint
from helpers import (
    get_user_answer,
    get_congratulations,
    check_answer,
    generate_progression
)
from helpers import MAX_ROUNDS


def get_element_index(progression):
    element_index = randint(0, len(progression))
    return element_index


def get_element_val(progression, element_index):
    element_val = str(progression[element_index])
    return element_val


def get_changed_progression(progression, element_val):
    progression = " ".join(map(str, progression))
    changed_progression = progression.replace(str(element_val), '..', 1)
    return changed_progression


def brain_progression(player_name):
    print('What number is missing in the progression?')

    rounds = 0
    correct_rounds = 0
    while rounds < MAX_ROUNDS:
        progression = generate_progression()
        element_index = get_element_index(progression)
        element_val = get_element_val(progression, element_index)
        changed_progression = get_changed_progression(progression, element_val)
        answer = get_user_answer(changed_progression)
        correct_answer = element_val
        correct_rounds = check_answer(answer, correct_answer, rounds, player_name)
        rounds += 1
        if (correct_rounds != rounds):
            return correct_rounds
    return correct_rounds
    get_congratulations(player_name, correct_rounds)
