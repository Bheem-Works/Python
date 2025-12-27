class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        self.name = 'vim'  # Reassigning the name
        return f"Namaste, {self.name}!"

# Instantiate with a name
p1 = Person("miso")  # Provide an initial name
print(p1.greet())

# Using self again but renaming it 
class Cat:
    def __init__(miso,name,food,color):
        miso.name = name
        miso.food = food
        miso.color = color
    
    def info(abc):
        print("Hello i am " + abc.name+ ", i like to eat " + abc.food + " and my color is " + abc.color)

miso = Cat('miso','egg','calf')
print(miso.name,miso.food,miso.color)


# Call one method from another method using self:

class Student:
    def __init__ (self,name,adress):
        self.name = name
        self.adress = adress

    def greet(self):
        return "Hello " + self.name + ". "
    
    def introduce(self):
        michi = self.greet()
        print(michi + "Welcome to the terminal")

std = Student('miso','12th')
std.introduce()