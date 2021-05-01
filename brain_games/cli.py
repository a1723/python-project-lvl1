#!/usr/bin/env python

import prompt


def entering_user_name():
    welcome = prompt.string('May I have your name? ')
    name = print('Hello, ' + welcome + '!')
    return name
    
