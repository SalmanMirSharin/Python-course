
class RideManager:
    def __init__(self):
        print('Ride Manager activated')
        self.__income = 0
        self.__trip_history = [] 
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []

    def add_a_vehicle(self,vehicle_type, vehicle):
        if vehicle_type=='car':
            self.__available_cars.append(vehicle)
        elif vehicle_type=='bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)
    
    def get_available_car(self):
        return self.__available_cars


    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type=='car':
            vehicles = self.__available_cars
        elif vehicle_type=='bike':
            vehicles = self.__available_bikes
        else:
            vehicles = self.__available_cng

        if len(vehicles)==0:
            print('Sorry no car available now!')
            return False
        for vehicle in vehicles:
            # print(f'Protential',rider.location,car.driver.location)
            if abs(rider.location - vehicle.driver.location)<10:
                distance = abs(rider.location - destination)
                fare = distance*vehicle.rate
                if rider.balance <fare:
                    print("you don't have enough money!",fare,rider.balance)
                    return False
                if vehicle.status=='available':
                    vehicle.status = 'unavailable'
                    trip_info = f'match {vehicle_type} for {rider.name} and fare: {fare} with driver {vehicle.driver.name} Started: {rider.location} To: {destination}'
                    print(trip_info) 
                    vehicles.remove(vehicle)
                    rider.start_a_trip(fare,trip_info)
                    vehicle.driver.start_a_trip(rider.location,destination,fare*0.8,trip_info)
                    self.__income += fare*0.2
                    self.__trip_history.append(trip_info)
                       
                                            
                    return True


uber = RideManager()