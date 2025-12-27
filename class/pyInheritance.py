
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Person:
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
    
    def printName(self):
        return f"{self.firstName} {self.lastName}"

class callPerson(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x = callPerson('vim','magar')
print(x.printName())


# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Cat:
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
    
    def catName(self):
        return f"{self.firstName} {self.lastName}"

class CallCat(Cat):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        # Creating the new variable through using the self 
        self.left = '5 months ago'

Y = CallCat('kim','miso')
print(Y.catName())
print(Y.left)

