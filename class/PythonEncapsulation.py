
#Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.

class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    
    # Getter method to access age
    def get_age(self):
        return self._age
    
    # Setter mthod to set age with validation 
    def set_age(self,age):
        if age > 0:
            self._age = age 
        else:
            print("Invalid age sorry ")


p1 = Person("vim",23)
print(p1.get_age())

p1.set_age(30)
print(p1.get_age())



class Student:
    def __init__(self,name):
        self.name = name
        self._grade = 0

    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self._grade = grade
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.") 
    
    def get_grade(self):
        return self._grade

    def is_passing(self):
        if self._grade >= 60:
            print("passed!")
        else:
            print("failed!")

student = Student("Vim")
student.set_grade(85)
print(student.get_grade())
print(student.is_passing())
