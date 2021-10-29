import random



def addition():
    answer = num1 + num2
    question = int(input("What is %s + %s? " % (num1, num2)))

    if answer == question:
        print("Well done!")
    else:
        print("Sorry, that is incorrect. " )


def subtraction():
    answer = num1 - num2
    question = int(input("What is %s - %s? " % (num1, num2)))

    if answer == question:
        print("Well done!")
    else:
        print("Sorry, that is incorrect. " )



def multiplication():
    answer = num1 * num2
    question = int(input("What is %s * %s? " % (num1, num2)))

    if answer == question:
        print("Well done!")
    else:
        print("Sorry, that is incorrect." )


num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
operators = random.randint(1, 3)

if operators == 1:
    addition()
elif operators == 2:
    subtraction()
else:
    multiplication()