
class SumAndPow:
    def __init__(self):
        self.sm = 0
        self.pw = 1

    def sum(self,*arg):
        for i in arg:
            self.sm+=i
        print(self.sm)
        
    def pow(self,n):
        for i in range(n):
            self.pw*=self.sm
        print(self.pw)

x = SumAndPow()
x.sum(1,3,5)
x.pow(2)

n = SumAndPow()
n.sum(1,3,4)
n.pow(3)
