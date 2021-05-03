#!/usr/bin/env python

import prompt


def entering_user_name():
    welcome = prompt.string('May I have your name? ')
    print("Hello, {}!".format(welcome))
    return welcome
    
