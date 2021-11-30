Calendar2021 = {
'january' : 31,
'february' : 28,
'march' : 31,
'april' : 30,
'may' : 31,
'june' : 30,
'july' : 31,
'august' : 31,
'september' : 30,
'october' : 31,
'november' : 30,
'december' : 31
}

monthName=str(input("Please enter a month name: "))
monthName=monthName.lower()

if monthName in Calendar2021:
 print('\nThe month ',monthName,' has ',Calendar2021[monthName],'days\n')
else:
 print("the month doesnt exist")

sortedkeys = sorted(Calendar2021)
print('\nThe months in alphabetical order:\n')
for i in sortedkeys:
 print(i)

print("\nAll months with 31 days are as under: \n")
for month in Calendar2021:
 if Calendar2021[month]==31:
  print(month)

sortedByValues=sorted(Calendar2021.items(), key=lambda x: x[1])

print("\nThe (key-value) pairs sorted by the number of days in each month are as under.\n")

for i in range(len(sortedByValues)):
 print(sortedByValues[i])        