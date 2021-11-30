def sum_digits(n):
    x = sum(int(n) for n in str(n))
    y = sum(int(x) for x in str(x))
    z = sum(int(y) for y in str(y))
    print(z)

sum_digits(77777)
