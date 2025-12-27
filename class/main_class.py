class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("miso",17)
print(p1.name,p1.age) 

# create a class without init 
class Car:
    pass
car1 = Car()
car1.brand = "Toyota"
car1.model = "Corolla"

print(car1.brand,car1.model)

# but with using the init method it easier to create object with the initial value 

