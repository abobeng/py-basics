
for x in range(10):
 username =input('enter user name: ')
 password = int(input('password: '))
 x[username] = password

print(x)

while True:
 username =input('\nEnter your username: ')
 password =int(input('\nEnter your password'))
 if password in my_dict:
  print('you have been logged in to the system')
 else:
  print('invalid password')