def first_diff(string1, string2):
    x=string1.split()
    y=string2.split()
    if len(x)<len(y):
        length=len(y)
    else: length=len(y)
    for i in range (length):
        if x[int(i)] == y[int(i)]:
            print('the location of the string name')
        else:
            b=x[i]
            print('the location of string different at:' )

string1='hello you are learning python now'
string2='hello you are good in learning'

first_diff(string1, string2)
