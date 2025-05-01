from base.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def move(self):
        print(f"{self.make} {self.model} is Driving 🚗")

    def start_engine(self):
        print(f"{self.make} {self.model}'s engine started.")
