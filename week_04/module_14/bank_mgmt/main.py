"""Manage Bank Account"""

class Account:
    accID = 1
    def __init__(self,name,age, nid_num, balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

        #update acc id
        self.account_id = Account.accID
        Account.accID+=1

    def deposit(self, amount):
        self.balance +=amount

    def withdraw(self,amount):
        self.balance -=amount

account_1 = Account('Mehedi',24,499,500)
account_2 = Account('kona',23,499,500)
# print(account_1.account_id)
# print(account_2.account_id)
print('Deposit')
account_1.deposit(2000)
account_2.deposit(1200)
print('acc_1',account_1.balance)
print('acc-2',account_2.balance)

print('Withdraw')
account_1.withdraw(100)
account_2.withdraw(300)
print('acc_1',account_1.balance)
print('acc_2',account_2.balance)
