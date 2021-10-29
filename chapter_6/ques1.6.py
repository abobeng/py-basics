num = input('enter a string:')
print('(a) The total number of characters in this string is:', len(num))
for i in range(10):
    print(num)
print('(c) the first character of the string is:',num[0])
print('(d) the first three characters of the sring are:', num[0:3])
print('(e) the last three characters of the string are:',num[-3:])
print('(f) the string backwards is:',num[::-1])
try :
    print('(g) the 7th character of string:',num[7])
except:
    print('(g) less than 7 characters')
print('(h) the string with first and last characters removed:',num[1:-1] )
print('(i) string in caps:', num.upper())
print('(j) every a letter replaced with e:', num.replace('a','e'))
print('(k) every letter replaced with space:', num.replace(num,''))
