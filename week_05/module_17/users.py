import hashlib
import random
from brta import BRTA
from vehicle import Car
from vehicle import Bike
from vehicle import Cng
from ride_manager import uber
import threading

license_authority = BRTA()

class UserAlreadyExists(Exception):
    def __init__(self,email, *args: object) -> None:
        print(f'The email {email} already exist!')
        super().__init__(*args)

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        pwd_encryped = hashlib.md5(password.encode()).hexdigest()
        already_exist = False
        with open('user.txt','r') as f:
            if email in f.read():
                already_exist = True
                # raise UserAlreadyExists(email)
        f.close()
        if already_exist ==False:
            with open('user.txt','a') as f:
                f.write(f'{self.email} {pwd_encryped}\n')
            f.close()
        # print(f'{self.name} User created!')

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
        self.__trip_history = []
        super().__init__(name,email,password)

    def set_location(self,location):
        self.location = location
    
    def get_location(self):
        return self.location

    def request_trip(self,destination):
            pass
    
    def get_trip_history(self):
        return self.__trip_history
    
    def start_a_trip(self,fare,trip_info):
        print(f'A trip star for {self.name}')
        self.balance -=fare
        self.__trip_history.append(trip_info)



class Driver(User):
    def __init__(self, name, email, password,location,license):
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(self.email,self.license)
        self.balance = 0
        self.vehicle = None

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result ==False:
            # print('Sorry you failed, try again!')
            self.license = None
        else:
            self.license = result
            self.valid_driver = True
    
    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            if vehicle_type=='car':
                self.vehicle =Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type=='bike':
                self.vehicle =Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            else:
                self.vehicle =Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
        else:
            pass

    def start_a_trip(self,start,destination,fare,trip_info):
        self.balance +=fare
        self.location = destination
        # Start thread:
        trip_thread = threading.Thread(target=self.vehicle.start_driving,args=(start,destination,))
        trip_thread.start()
        # self.vehicle.start_driving(start,destination)
        self.__trip_history.append(trip_info)

    


    

rider1 = Rider('rider1','rider1@gmail.com','rider1', random.randint(0,30),1000)
rider2 = Rider('rider2','rider2@gmail.com','rider2', random.randint(0,30),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3', random.randint(0,30),5000)
rider4 = Rider('rider4','rider4@gmail.com','rider4', random.randint(0,30),5000)


# rider1 = Rider('rider1','rider1@gmail.com','rider1', random.randint(0,30),5000)
# rider2 = Rider('rider2','rider2@gmail.com','rider2', random.randint(0,30),5000)
# rider3 = Rider('rider3','rider3@gmail.com','rider3', random.randint(0,30),5000)
# rider4 = Rider('rider4','rider4@gmail.com','rider4', random.randint(0,30),5000)

vehicle_types = ['car','bike','cng']

for i in range(1,100):
    driver1 = Driver(f'driver{i}',f'driver{i}@gmail.com',f'driver{i}',random.randint(0,100),random.randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(random.choice(vehicle_types),random.randint(10000,99999),10)


print(uber.get_available_car())

uber.find_a_vehicle(rider1,random.choice(vehicle_types),random.randint(1,100))
uber.find_a_vehicle(rider2,random.choice(vehicle_types),random.randint(1,100))
uber.find_a_vehicle(rider3,random.choice(vehicle_types),random.randint(1,100))
uber.find_a_vehicle(rider4,random.choice(vehicle_types),random.randint(1,100))

print(rider1.get_trip_history())
print(uber.total_income())