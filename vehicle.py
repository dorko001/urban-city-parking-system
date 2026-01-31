class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def get_type(self):
        return "Vehicle"


class Car(Vehicle):
    def get_type(self):
        return "Car"


class Motorcycle(Vehicle):
    def get_type(self):
        return "Motorcycle"
