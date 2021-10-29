temp = float(input('enter a temperature in Celsius:'))
if temp < -273.15:
    print ('The temperature is invalid because it is below absolute zero')
if temp == -273.15:
    print('the temperature is absolute 0')
if -273.15 < temp < 0:
    print('the temperature below is freezing')
if temp == 0:
    print('the temperature is at the freezing point')
if 0 < temp <100:
    print('temperature is in normal range')
if temp ==100:
    print('temperature is at the boiling point')
if temp > 100:
    print('the temperature is above the boiling point')
