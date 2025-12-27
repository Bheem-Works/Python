
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same fname that can be executed on many objects or classes.

class Car:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def move(self):
        print("move")

class Ship:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def move(self):
        print("sail")

class Plane:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def move(self):
        print("fly")

car1 = Car("BMW",240)
ship1 = Ship("Titanic",40)
plane1 = Plane("Boeing",900)

for x in (car1,ship1,plane1):
    print(f"{x.name} moves at speed {x.speed}")
    x.move()  # Polymorphism in action
    print('')

class Vechile:
    def __init__ (self,fname,brand):
        self.fname = fname
        self.brand = brand

    def move(self):
        print('move')
    
class Bike(Vechile):
    pass

class Boat(Vechile):
    # def __init__(self,fname,brand):
    #     super().__init__(fname,brand)
    def move(self):
        print('sail')

class Aeroplane(Vechile):
    def move(self):
        print('fly')

Bike1 = Bike("Ducati","Ducati Inc.")
Boat1 = Boat("Queen Mary","Cunard Line")
Aeroplane1 = Aeroplane("Airbus","Airbus SE")

for x in (Bike1,Boat1,Aeroplane1):
    print(x.fname)
    print(x.brand)
    print('')
    