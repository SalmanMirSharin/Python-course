class Phone:

    manufacture = 'China'

    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def sum(self,a,b):
        return a+b


my_phone = Phone('Oppo','blue','14000')

print(my_phone.brand,my_phone.manufacture)

your_phone = Phone('iPhone','purple','85000')

print(your_phone.brand,your_phone.manufacture)

dad_phone = Phone('Nokia','black','1500')
print(my_phone.price,your_phone.price,dad_phone.price)

sum = my_phone.sum(2,6)
print(sum)