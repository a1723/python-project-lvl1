#!/usr/bin/env python

from random import randint
from brain_games.engine import generate_number, get_user_answer, get_congratulations, check_answer, generate_progression

def get_mutable_element_index(progression):
    mutable_element_index = randint(0, len(progression))
    return mutable_element_index

def get_mutable_element_value(progression, mutable_element_index):
    mutable_element_value = str(progression[mutable_element_index])
    return mutable_element_value

def get_changed_progression(progression, mutable_element_value):
    changed_progression = " ".join(map(str, progression))
    print(changed_progression)
    changed_progression = changed_progression.replace(str(mutable_element_value), '..', 1)
    return changed_progression


def main():
    print('What number is missing in the progression?')

    count_correct_answers = 0
    while count_correct_answers < 3:
        progression = generate_progression()
        mutable_element_index = get_mutable_element_index(progression)
        mutable_element_value = get_mutable_element_value(progression, mutable_element_index)
        changed_progression = get_changed_progression(progression, mutable_element_value)
        answer = get_user_answer(changed_progression)
        correct_answer = mutable_element_value
        count_correct_answers = check_answer(answer, correct_answer, count_correct_answers)
    get_congratulations()
