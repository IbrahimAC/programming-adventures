"""Encapsulation"""

class privateMethod:
    def __init__(self):
        self.__attr = 1
    def __printHi(self):
        print("hi")
    def printHello(self):
        print("hello")

a = privateMethod()
a.printHello()
a.__printHi()
a.__attr

#Output

#Hello
#AttributeError: 'PrivateMethod' object has no attribute '__printhi'
#AttributeError: 'PrivateMethod' object has no attribute '__attr

#As we can see, it’s as if the method and attribute do not exist, thus we get an error.
#In order to access and modify private attributes, we use getter and setter methods
