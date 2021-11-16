from random import randint

points = 100
while 0 < points < 200:
    r = randint(1, 10)
    guess = eval(input('Your guess: '))
    if guess < r:
        points -= 10
        print('Too low.', end=' ')
    elif guess > r:
        points -= 20
        print('Too high.', end=' ')
    else:
        points += 100
        print('Right!', end=' ')
    print('Score:', points)
if points >= 200:
    print('You win!')
else:
    print('You lose.')

