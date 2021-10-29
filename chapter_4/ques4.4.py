credit = int(input('how many credits have you taken:'))
if credit <= 23:
    print('you are a freshman')
if 24 <= credit <=53:
    print('you are a sophomore')
if 54 <= credit <= 83:
    print('you are a junior')
if credit >= 84:
    print('you are a senior')