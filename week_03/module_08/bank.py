

class Bank:

    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def withdraw(self,ammount):
        if ammount<self.min_withdraw:
            return f'No money for you, min-withdraw: {self.min_withdraw}'
        elif ammount>self.max_withdraw:
            return f'You crossed the max-limit: {self.max_withdraw}'
        elif ammount>self.balance:
            return f'You are broke!!! No money for you, you have: {self.balance} tk.'
        else:
            self.balance = self.balance-ammount
            return f'Here is your money: {ammount}'
    
    def deposit(self,ammount):
        self.balance = self.balance+ammount

my_bank = Bank(9000)

reply = my_bank.withdraw(100)
print(reply)

balance = my_bank.get_balance()
print(balance)

my_bank.deposit(5000)

print(my_bank.get_balance())

