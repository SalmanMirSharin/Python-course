class Boys:
    def __init__(self):
        self.boy1 = 100
        self.boy2 = 100
        self.boy3 = 100
        self.__boy4 = 0
        self.boy5 = 100

    @property
    def not_pay(self):
        return self.__boy4
    @not_pay.setter
    def not_pay(self,value):
         self.__boy4 = value

by = Boys()
by.not_pay = 1000
print(by.not_pay)



        

        
        
    
            
