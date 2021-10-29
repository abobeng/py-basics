from random import randint
num = randint(1,10)
guess = int(input('Enter your guess: '))
if guess==num:
    print('correct guess')
if guess!=num:
    print('wrong guess')