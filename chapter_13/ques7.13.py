def number(n):
    a=10**int(n-1)
    b=10**(n)-1
    from random import randint
    sol=randint(int(a), int(b))
    print(sol)

number(5)