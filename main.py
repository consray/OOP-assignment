# main.py

from vehicles.car import Car
from vehicles.electric_car import ElectricCar
from vehicles.plane import Plane
from vehicles.boat import Boat

vehicles = [
    Car("Toyota", "Corolla", 2020, "Blue"),
    ElectricCar("Tesla", "Model S", 2023, "Red", 100),
    Plane(),
    Boat()
]

for v in vehicles:
    v.move()
