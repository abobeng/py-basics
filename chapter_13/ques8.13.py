def number_of_factors(n):
    for i in range(1,n):
        if n%i==0:
            print('the factors are:', i)

number_of_factors(12)