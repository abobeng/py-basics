count = 0
for i in range(1, 101):
    if (i*i)%10 == 4:
        count = count + 1
    if (i*i)%10 == 9:
        count = count + 1
print (count)
