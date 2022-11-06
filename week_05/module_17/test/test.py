class Rider:
    def __init__(self,location,balance):
        self.location = location
        self.balance = balance

    def set_location(self,val):
        self.locatio = val

r = Rider('Jessore','100')

print(r.location)

r.set_location('Keshabpur')
print(r.location)