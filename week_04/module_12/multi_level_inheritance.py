class vehicle:
    def __init__(self,name, license, price):
        self.name = name
        self.license = license
        self.price =price

    def start(self):
        print(f'{self.name} started')
    
class Bus(vehicle):
    def __init__(self,name,license,price, seat,ticket_price):
        self.seat = seat
        self.abileable_seat = seat
        self.ticket_price = ticket_price
        print('Bus init called')
        super().__init__(name,license,price)

    def sell_ticket(self,customer_name, quantity, amount):
        self.abileable_seat -=quantity
        remainder = amount-self.ticket_price*quantity
        if remainder>=0:
            return Ticket(customer_name)
        else:
            return 'Not ticket for you.'

class ACBus(Bus):
    def __init__(self):
        print('AC bus created')

class MiniBus(Bus):
    def __init__(self):
        print('mini bus created')
        super().__init__('Mini mini','38994ds',1200000,50,450)
        #super().sell_ticket('any',1,400)
        

class Ticket:
    def __init__(self,owner):
        self.owner = owner


mini = MiniBus()
print(mini.name) 