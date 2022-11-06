import hashlib
import random
from brta import BRTA
from vehicle import Car
from vehicle import Bike
from vehicle import Cng
from ride_manager import uber

license_authority = BRTA()

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        pwd_encryped = hashlib.md5(password.encode()).hexdigest()
        # with open('user.txt','r') as f:
        #     content = f.readlines()
        #     for i,line in enumerate(content):
        #         compair = content[i].split(' ')
        #         if compair[0] !=email and compair[1]!=pwd_encryped:
        with open('user.txt','a') as f:
            f.write(f'{self.email} {pwd_encryped}\n')
        f.close()
        print(f'{self.name} User created!')
                     
             
    @staticmethod
    def log_in(email,password):
        read_pwd =''
        with open('user.txt','r') as f:
            lines = f.readlines()
            for line in lines:
               read_pwd = line.split(' ')[1]
        f.close()

        hash_pwd = hashlib.md5(password.encode()).hexdigest()
        if read_pwd==hash_pwd:
            print('right user!')
            return True
        else:
            print('wrong user!')
            return False
        # print('Password found:',read_pwd)



class Rider(User):
    def __init__(self,name,email,password,location,balance):
        self.location = location
        self.balance = balance
        super().__init__(name,email,password)

    def set_location(self,location):
        self.location = location
    
    def get_location(self):
        return self.location

    def request_trip(self,destination):
            pass
    
    def start_a_trip(self,fare):
        self.balance -=fare


class Driver(User):
    def __init__(self, name, email, password,location,license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(self.email,self.license)
        self.balance = 0

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result ==False:
            print('Sorry you failed, try again!')
        else:
            self.license = result
            self.valid_driver = True
    
    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            if vehicle_type=='car':
                new_vehicle =Car(vehicle_type,license_plate,rate,self.email)
                uber.add_a_vehicle(vehicle_type,new_vehicle)
            elif vehicle_type=='bike':
                new_vehicle =Bike(vehicle_type,license_plate,rate,self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle =Cng(vehicle_type,license_plate,rate,self.email)
                uber.add_a_vehicle(vehicle_type,new_vehicle)


    def start_a_trip(self,destination,fare):
        self.balance +=fare
        self.location = destination

    


    

rider1 = Rider('rider1','rider1@gmail.com','rider1', random.randint,5000)
rider2 = Rider('rider2','rider2@gmail.com','rider2', random.randint,5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3', random.randint,5000)
rider4 = Rider('rider4','rider4@gmail.com','rider4', random.randint,5000)


driver1 = Driver('driver1','driver@gmail.com','driver1',random.randint(0,100),1253)
driver1.take_driving_test()
driver1.register_a_vehicle('car',5462,10)
driver2 = Driver('driver2','driver@gmail.com','driver2',random.randint(0,100),1253)
driver3 = Driver('driver3','driver@gmail.com','driver3',random.randint(0,100),1253)
driver4 = Driver('driver4','driver@gmail.com','driver4',random.randint(0,100),1253)