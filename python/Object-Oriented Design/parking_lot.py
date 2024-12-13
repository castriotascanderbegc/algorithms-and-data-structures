"""
    Parking lots have open spaces for vehicles to park in. Vehicles can be of different sizes, e.g. cars, limos, trucks, etc.
    In some cases, parking spots can be numbered. For large venues, parking lots may have multiple levels, i.e. parking garages.
    Sometimes parking is free, but in other cases customers have to pay. So parking lots can have a payment system to keep track of parked vehicles.

    
    Basics
        Multiple levels in the parking lot
        Possible vehicle types: car, limo, semi-truck
        We will have a payment system, with a single entrance and exit
        Drivers will be assigned a parking spot after paying
    Vehicles and Parking Spots
        Vehicles can be of different sizes (car = 1, limo = 2, truck = 3)
        Each parking spot will have a size of 1
        A vehicle must fully take up each spot assigned to it (no fractional spots)
        Vehicles will automatically be assigned the next available parking spot on the lowest floor
    Payment System
        Drivers will pay for parking and be assigned the next available spot on the lowest floor
        Drivers can pay for a variable number of hours and they are charged after they remove their vehicle based on an hourly rate
        We can assume vehicles can be parked for a variable number of hours
        If there is no capacity, the system should not assign a spot and should notify the driver
"""

# A Vehicle class will be the base class for all vehicles. 
# It will have a size attribute that will be used to determine how many spots it will take up.
class Vehicle:
    def __init__(self, size):
        self._spot_size = size

    def get_spot_size(self):
        return self._spot_size

# Cars, Limos, and SemiTrucks will inherit from the Vehicle class. Each will have a predefined size.
class Car(Vehicle):
    def __init__(self):
        super().__init__(1)

class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(3)
        

# A Driver class will have a vehicle that belongs to it, and a total payment due. 
# It will also have a method to charge the driver for parking.
class Driver:
    def __init__(self, id, vehicle):
        self._id = id
        self._vehicle = vehicle
        self._payment_due = 0

    def get_id(self):
        return self._id
    
    def get_vehicle(self):
        return self._vehicle
    
    def charge(self, amount):
        self._payment_due += amount
    

# A ParkingFloor will be the container for parking spots, which will be represented by an array. 
# It will also keep track of which vehicles are parked in which spots, where [l, r] represents the range of spots occupied by a vehicle.
class ParkingFloor:
    def __init__(self, number_of_spots):
        self._spots = [0] * number_of_spots
        self._vehicle_map = {}
    
    def park_vehicle(self, vehicle):
        # get the size of the vehicle
        size = vehicle.get_spot_size()
        # apply a fixed size sliding window technique with 2 pointers
        l, r = 0, 0
        while r < len(self._spots):
            # keep expanding until we reach our desired parking spot size
            
            # if current spot is not empty, we can directly move L next to R
            if self._spots[r] != 0:
                l = r + 1
            # if we found empty spots of desired size, we can mark these as occupied
            if r - l + 1 == size:
                for k in range(l, r + 1):
                    self._spots[k] = 1
                # insert vehicle in our map with its range of parking spots
                self._vehicle_map[vehicle] = [l, r]
                return True
            r += 1
        return False
    
    def remove_vehicle(self, vehicle):
        start, end = self._vehicle_map[vehicle] # retrieve range of parking spots occupied by given vehicle 
        for i in range(start, end + 1):         # iterate from start to end and mark these spots with a 0
            self._spots[i] = 0
        del self._vehicle_map[vehicle]          # del the vehicle entry from the map

    def get_parking_spots(self):
        return self._spots
    
    def get_vehicle_map(self):
        return self._vehicle_map
    
    def get_vehicle_spots(self, vehicle):
        return self._vehicle_map.get(vehicle)
    


# A ParkingGarage will contain an arbitrary number of ParkingFloors.
# Notice how spots_per_floor is passed into the ParkingFloor constructor. 
# This is because we want to be able to have different sized parking floors. But what if each floor had a varying number of parking spots? We could pass in an array of spots_per_floor instead.
class ParkingGarage:
    def __init__(self, floor_count, spots_per_floor):
        self._floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]
    
    def park_vehicle(self, vehicle):
        for floor in self._floors:
            if floor.park_vehicle(vehicle):
                return True
        return False
    
    def remove_vehicle(self, vehicle):        
        for floor in self._floors:
            if floor.get_vehicle_spots(vehicle):
                floor.remove_vehicle(vehicle)
                return True
        return False


# The ParkingSystem will be the main controller of the ParkingGarage. 
# It will be responsible for tracking parking hours and charging drivers.

import datetime
import math

class ParkingSystem:
    def __init__(self, parkingGarage, hourlyRate):
        self._parking_garage = parkingGarage
        self._hourly_rate = hourlyRate
        self._time_parked = {}  # map driver id to time they originally parked
    
    def park_vehicle(self, driver):
        current_hour = datetime.datetime.now().hour
        isParked = self._parking_garage.park_vehicle(driver.get_vehicle())
        if isParked:
            self._time_parked[driver.get_id()] = current_hour
        return isParked
    
    def remove_vehicle(self, driver):
        if driver.get_id() not in self._time_parked:
            return False
        current_hour = datetime.datetime.now().hour
        time_parked = math.ceil(current_hour - self._time_parked[driver.get_id()])
        driver.charge(time_parked * self._hourly_rate)

        del self._time_parked[driver.get_id()]
        return self._parking_garage.remove_vehicle(driver.get_vehicle())
    


###########

parkingGarage = ParkingGarage(3, 2)
parkingSystem = ParkingSystem(parkingGarage, 5)

driver1 = Driver(1, Car())
driver2 = Driver(2, Limo())
driver3 = Driver(3, Truck())

print(parkingSystem.park_vehicle(driver1))      # true
print(parkingSystem.park_vehicle(driver2))      # true
print(parkingSystem.park_vehicle(driver3))      # false

print(parkingSystem.remove_vehicle(driver1))    # true
print(parkingSystem.remove_vehicle(driver2))    # true
print(parkingSystem.remove_vehicle(driver3))    # false