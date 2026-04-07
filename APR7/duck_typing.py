class Bike:
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels

    def no_of_wheels(self):
        return f"For Bike number of Wheels are: {self.wheels}"

class Car:
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels

    def no_of_wheels(self):
        return f"For Car number of Wheels are: {self.wheels}"

def show_wheels(vehicle):
    print(vehicle.no_of_wheels())   

bike_obj = Bike("NS200", 2)
car_obj = Car("Etios", 4)

show_wheels(bike_obj)
show_wheels(car_obj)