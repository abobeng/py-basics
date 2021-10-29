print('the perfect numbers between 1 and 10000 are:')
for i in range(1, 1001):
    sum = 0
    if (i % i == i):
        print(i)