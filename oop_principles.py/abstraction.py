"""Abstraction"""

#Here, the class 'ABC' is imported to and inherited by the class 'shape'.
#The class 'Shape' becomes an abstract class when we define abstract methods in it.
#As we already discussed, abstract methods should not contain any implementation.
# So, we can define abstract methods using the 'pass' statement' as shown below.

from abc import ABC
class Shape(ABC): #abstract classdef calculate_area(self): #abstract methodpass
    pass

class Rectangle(Shape):
    length = 5
    breadth = 3
    def calculate_area(self):return self.length * self.breadth

class Circle(Shape):
    radius = 4
    def calculate_area(self):return 3.14 * self.radius * self.radius

rec = Rectangle() #object created for the class 'Rectangle'
cir = Circle() #object created for the class 'Circle'
print("Area of a rectangle:", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'
print("Area of a circle:", cir.calculate_area()) #call to 'calculate_area' method defined inside the class 'Circle'.
# Output:
# Area of a rectangle: 15
# Area of a circle: 50.24

#If the implementation of the abstract method is not defined in the derived classes, then the Python interpreter throws an error.

from abc import ABC
class Shape(ABC):

    def print(self):
        print("I am a normal method defined inside the abstract class 'Shape'")

    def calculate_are(self):
        pass

class Rectangle(Shape):
    length = 5
    breadth = 3

    def calculate_area(self):
        return self.length * self.breadth

#Here the normal method is called from the main() method using an object created for the child class 'Rectangle'.
rec = Rectangle() #object created for the class 'Rectangle'
rec.print()
print("Area of a rectangle:", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'

# Output:
# I am a normal method defined inside the abstract class 'Shape'