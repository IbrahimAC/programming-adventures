"""Polymorphism"""

class Animal:
    def eat(self):
        print("{} is eating slowly".format(self.__class__.__name__))

class Dog(Animal):
    def eat(self):
        print("Dog is eating super fast")

class Cat(Animal):
    pass
#Now we can instantiate these classes into two objects, and run the method.

jack = Dog()
jill = Cat()
jack.eat()
jill.eat()
#Output
"Dog is eating super fast"
"Cat is eating slowly"

#A true example to show polymorphism would be iterating through different objects:
for animal in (jack, jill):
    animal.eat()

#Output:
"Dog is eating very fast"
"Cat is eating slowly"

#The for loop first iterates through the instantiation of the Dog class first, and the Cat class after.
# This is why we see the output of the Dogs methods before the Cats methods