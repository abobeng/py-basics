class Product:
    def __init__ (self, name, amount, price):
        self.name=name
        self.amount=amount
        self.price=price

    def get_price(self):
        return 'Regular Price: ', self.amount*self.price

    def make_purchase(self):
        if self.amount<10:
            print(f"Discount Price {self.amount * self.price}")
        elif (self.amount >= 10 and self.amount < 100):
            return 'Discount price : ', self.amount * self.price -(t(self.amount*self.price*10/10))
        elif self.amount>100:
            return 'Discount price: ', a*p-(a*p*20/100)
        else
            return "nothing to return"

name=input('Product . Name : ')
amount=eval(input('No. of items bought : '))
price=eval(input('price of pdt: '))

product = Product(name, amount, price)
product = { name: ""}
# print (c.get_price())
# print (c.make_purchase())