
# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.


class Outer:
    def __init__(self):
        self.name = 'outer class'

    class Inner:
        def __init__(self):
            self.name = 'inner class'
    
        def display(self):
            print('this is inner class')

outer = Outer()
inner = outer.Inner()
inner.display()

# Pratical example 

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine(self)
    
    class Engine:
        def __init__(self, car):
            self.status = 'off'
            self.car = car
        def start(self):
            self.status = 'running'
            print('engine started')
        def stop(self):
            self.status = 'off'
            print('engine stopped')
        
        def drive(self):
            if self.status == 'running':
                print(f"Driving the {self.car.brand} {self.car.model}")
            else:
                print("Start the engine first!")

car = Car('Toyota','Camry')
car.engine.drive()
car.engine.start()
car.engine.drive()        


# Multiple inner class 

class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()
    
    class CPU:
        def process(self):
            print("CPU is processing data")
    
    class RAM:
        def load(self):
            print("RAM is loading data")

computer = Computer()
print(computer.cpu.process())
print(computer.ram.load())

