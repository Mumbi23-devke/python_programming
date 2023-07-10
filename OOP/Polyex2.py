class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
            print("Driving around")


class Plane:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
            print("Flying around")


class Motorbike:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
            print("Biking around")


# Instance of our class
car = Car("Honda", "CX-5")
plane = Plane("Boeing", "737")
bike = Motorbike("Kawasaki", "Ninja 650")

for i in (car, plane, bike):
    i.move()
