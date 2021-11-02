
integers_list = input('enter integers separated by space ')
lst = integers_list.split( )
print(lst)

print('number of elements in the list is : ',len(lst))

print(lst[::-1])
print(lst[-1])

for i in lst: 
    if i == '5':
        print('yes')
    else:
        print('no')


lst.count('5')

lst[:-1]
print(lst)
lst[0:4]
print(lst)

lst.sort()
print(lst)



