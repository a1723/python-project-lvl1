import prompt


def entering_user_name():
    welcome = prompt.string('May I have your name? ')
    print(f'Hello, {welcome}!')
    return welcome
    
