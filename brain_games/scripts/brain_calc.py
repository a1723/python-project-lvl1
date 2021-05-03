#!/usr/bin/env python

from brain_games.engine import prompt, choice, randint, name, generate_number, summa, difference, multiplication, funcs


def main():
    print('What is the result of the expression?')

    correct_answers = 0
    while correct_answers < 3:
        a = generate_number()
        b = generate_number()
        rand_func = (choice(funcs))
        if(rand_func == summa):
            
            answer = prompt.string('Question: {0} + {1}{2}Your answer: '.format(a, b, '\n'))
            
            if (answer == summa(a, b)):
                print('Correct!')
                correct_answers += 1
            else:
                print("'{0}' is wrong answer ;(. Correct answer was '{1}'{2}Let\'s try again, {3}!".format(answer, summa(a, b), '\n',  name))
                return   
        
        elif(rand_func == difference):
            
            answer = prompt.string('Question: {0} - {1}{2}Your answer: '.format(a, b, '\n'))
            
            if (answer == difference(a, b)):
                print('Correct!')
                correct_answers += 1
            else:
                print("'{0}' is wrong answer ;(. Correct answer was '{1}'{2}Let\'s try again, {3}!".format(answer, difference(a, b), '\n',  name))
                return   
            
        elif(rand_func == multiplication):
            
            answer = prompt.string('Question: {0} * {1}{2}Your answer: '.format(a, b, '\n'))
            
            if (answer == multiplication(a, b)):
                print('Correct!')
                correct_answers += 1
            else:
                print("'{0}' is wrong answer ;(. Correct answer was '{1}'{2}Let\'s try again, {3}!".format(answer, multiplication(a, b), '\n',  name))
                return
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()