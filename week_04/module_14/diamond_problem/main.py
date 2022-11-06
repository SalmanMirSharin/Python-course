'''Diamond ring problem'''

class A:
    def print_somthing(self):
        print('Im on A')

class B(A):
    # def print_somthing(self):
    #      print('Im on B') 
    pass
         

class C(A):
    # def print_somthing(self):
    #      print('Im on C') 
    pass
class D(B,C):
    pass


obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.print_somthing()
obj2.print_somthing()
obj3.print_somthing()
obj4.print_somthing()


