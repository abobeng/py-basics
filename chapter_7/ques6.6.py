s = input('enter a string:')
s = s.lower()
for c in '.':
    s = s.replace(c, '')
print(s)
