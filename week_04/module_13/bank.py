class Account:
    def __init__(self,holder,initial_balance) -> None:
        self.holder = holder
        self.balacne = initial_balance
    
    def deposit(self,amount):
        self.balacne +=amount
    
    def withdraw(self,amount):
        self.balacne -=amount


class StudentAccount(Account):
        def __init__(self,holder,initial_balance,school):
            self.school = school
            super().__init__(holder,initial_balance)

rafsan = StudentAccount('Rafi',50000,'IUB')   

            
         