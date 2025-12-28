
#Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.

class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    
    def get_age(self):
        return self._age

p1 = Person("vim",23)
print(p1.get_age())
