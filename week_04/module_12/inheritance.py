#laptop, phone, watch, tablet,

class Device:
    def __init__(self,brand,price, color):
        self.brand = brand
        self.price =price
        self.color = color

    def re_sale(self):
        print('ready to sale again')
        


class Laptop(Device):
    def __init__(self,brand,price, color, disc_size) -> None:
        super().__init__(brand,price,color)
        # self.brand = brand
        # self.price =price
        # self.color = color
        self.disc_size =disc_size
    
    def run(self):
        print('ruccing the laptop')

    def __repr__(self) -> str:
        return f'Laptop {self.brand} and price {self.price} and color {self.color}'
    def purchase(self, money,discount):
        if money<(self.price* discount/100):
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money-self.price

class Phone:
    def __init__(self,brand,price, color, camera,sim_num) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num
    
    def __repr__(self) -> str:
        return f'Phon {self.brand} and price {self.price} and color {self.color}'


    def purchase(self, money):
        if money<self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money-self.price


    def is_dul_sim(self):
        return self.sim_num>1

class Watch:
    def __init__(self,brand, price, color,watch_type) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type
   
    def purchase(self, money):
        if money<self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money-self.price


    def is_digital(self):
        return self.watch_type=='digital'



class Manager:
    def __init__(self,name, salary, experience, designation) -> None:
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass

class SalesPerson:
    def __init__(self, name, salary, experience, designation, comission) -> None:
        pass

    def withdraw_salary(self):
        pass

    def handle_customer_complane(self):
        pass 
    
    def handle_customer(self):
        pass

lenovo = Laptop('Lenovo',45000,'black','500gb')
hp = Laptop('HP',35000,'silver','250gb')
print(lenovo)
print(hp)

opp = Phone('Opp',1500,'black','15mp',2)
samsung = Phone('Samsung',21000,'Silver','12mp',1)
print(opp)
print(samsung)

hp.re_sale()
print(hp.brand)
