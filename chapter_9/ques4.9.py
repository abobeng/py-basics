for password_try in range(5):
    password = '123qwert'
    password_try = input('enter a password: ')
    if password_try == password:
        print('you are logged into system')
        break
    elif password_try != password:
        print('re enter password, wrong password ')
    else :
         print('you have been kicked out of the system')

