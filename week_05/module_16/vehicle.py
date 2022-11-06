from abc import ABC,abstractmethod

class Vehicle(ABC):

    speed = {
            'car':30,
            'bike':50,
            'cng': 20,

        }

    def __init__(self,vehicle_type,license_plate,rate,driver) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'
        self.speed = self.speed[vehicle_type]
        self.driver = driver

    @abstractmethod
    def start_driving(self):
        pass
    
    @abstractmethod
    def trip_finished(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver,) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate,'started')
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.license_plate,'compled trip')
        return super().trip_finished()

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver,) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate,'started')
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.license_plate,'compled trip')
        return super().trip_finished()

class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver,) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate,'started')
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.license_plate,'compled trip')
        return super().trip_finished()
        

