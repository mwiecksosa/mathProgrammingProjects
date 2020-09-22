class Zp:
    def __init__(self,n,p):
        self.p = p
        self.n = n % p

    def __add__(self,other):
        return Zp(self.n + other.n, self.p)

    def __neg__(self):
        return Zp(-self.n, self.p)

    def __sub__(self,other):
        return Zp(self.n + (-other.n), self.p)

    def __mul__(self,other):
        return Zp(self.n * other.n, self.p)

    def __pow__(self,q):
        return Zp(self.n**q, self.p)

    def __div__(self,other):
        return Zp(self * (other**(self.p-2)), self.p)

    def __str__(self):
        return '%i (mod %i)' % (self.n, self.p)

    def atab(self):
        nrow, ncol = self.p + 1, self.p + 1
        atab = [[0 for x in range(nrow)] for y in range(ncol)]

        for i in range(self.p + 1):
            for j in range(self.p + 1):
                if i == 0 and j == 0:
                    atab[i][j] = '+'
                elif i == 0 and j != 0:
                    atab[i][j] = j - 1
                elif i != 0 and j == 0:
                    atab[i][j] = i - 1    
                else:
                    atab[i][j] = ((j - 1) + (i - 1)) % self.p
        for x in atab: print(*x, sep = " ")

    def mtab(self):
        nrow, ncol = self.p + 1, self.p + 1
        mtab = [[0 for x in range(nrow)] for y in range(ncol)]
        
        for i in range(self.p + 1):
            for j in range(self.p + 1):
                if i == 0 and j == 0:
                    mtab[i][j] = '*'
                elif i == 0 and j != 0:
                    mtab[i][j] = j -1
                elif i != 0 and j == 0:
                    mtab[i][j] = i - 1
                else:
                    mtab[i][j] = ((j - 1) * (i - 1)) % self.p
        for x in mtab: print(*x, sep = " ")
