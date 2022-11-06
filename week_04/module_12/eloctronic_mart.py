#laptop, phone, watch, tablet,

class Device:
    def __init__(self,brand,price, color):
        self.brand = brand
        self.price =price
        self.color = color

        


class Laptop:
    def __init__(self,brand,price, color, disc_size) -> None:
        self.brand = brand
        self.price =price
        self.color = color
        self.disc_size =disc_size
    
    def run(self):
        print('ruccing the laptop')

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
