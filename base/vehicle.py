# This is a base class for vehicles. It defines a method `move` that must be implemented by subclasses.
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")
