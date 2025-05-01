from vehicles.car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity
        self.charge_level = 100

    def move(self):
        print(f"{self.make} {self.model} is Driving silently with battery at {self.charge_level}% ⚡")
