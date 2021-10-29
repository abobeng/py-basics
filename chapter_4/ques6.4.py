n = int(input("Enter number of items: "))

cost = 1

if n < 10 :
    cost = n * 12
if 10 < n < 99 :
    cost = n * 10
if n > 100:
    cost = n * 7

print("Total Cost =", cost)