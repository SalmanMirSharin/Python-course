
balance = 600

def total_cost(price,quantity):
    global balance
    cost = price * quantity
    remaining = balance-cost
    balance = remaining
    
    return cost
print(balance)
pay = total_cost(10,3)
print(f'You have to pay {pay}')
print(balance)
