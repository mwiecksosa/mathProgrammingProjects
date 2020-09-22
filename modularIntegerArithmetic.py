#modular_integer.py

class Zp:
    def __init__(self,n):
        self.p = 7
        self.n = n % self.p

    def __add__(self,other): #the __ tell us it is a standard operator
        return Zp((self.n + other.n))

    def __neg__(self):
        return Zp(-self.n)

    def __sub__(self,other):
        return Zp(self.n + (-other.n)) #Left is obj oriented. This one isn't: Zp(self.n - other.n) 

    
    
