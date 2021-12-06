n = int(input('enter a number:'))
l = list()
for i in range(1, n+1):
    if n%i == 0:
        l.append(i)
print(l, 'are the list of the factors of', str(n) )