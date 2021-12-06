class Investment:
    def __init__(self,p,i,n):
        self.p=p
        self.i=i
        self.n=n

    def value_after(self):
        return ((self.p*(1+self.i))**self.n)

    def __str__(self):
        print('Principal-$:',self.p, 'Interest rate:', self.i,'%','Interes-$:',a.value_after())


a = Investment(1000,5.5,3)
(a.__str__())