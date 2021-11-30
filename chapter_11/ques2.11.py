numberOfProducts=int(input('Enter Number of products: '))
for x in range(numberOfProducts):
 productName=input('Product Name: ')
 PriceOfProduct = int(input('Price in : '))
 Dollaramount = int(input('enter a dollar amount : '))

 my_dict[productName] = PriceOfProduct

print(my_dict)

while True:
 productName=input('\nEnter a product name to know its price: ')
 if productName in my_dict:
  print('The price of ',productName, ' is ',my_dict[productName],' dollars.')
 else:
  print("The product you have entered doesn't exist")
  

  