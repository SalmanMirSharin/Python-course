
class Shopper:

    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})

    def checkout(self,amount):
        price =0
        for item in self.cart:
            print(item)
            price = price + item['price'] * item['quantity']
        if amount<price:
            return f'Please give me more money: {price-amount}'
        elif amount>price:
            return f'Here are the items and extra money: {amount-price}'
        else:
            return 'Here are the items!'

shopping = Shopper('Mr.Jhon')

shopping.add_to_cart('Shoes',500,3)
shopping.add_to_cart('T-Sharts',400,3)
shopping.add_to_cart('pants',700,3)

pay = shopping.checkout(4800)

print(pay)