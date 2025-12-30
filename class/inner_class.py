
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
