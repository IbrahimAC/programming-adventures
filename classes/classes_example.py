# Link to notes on classes --> https://docs.google.com/document/d/137_rd5jLXmiv9EvTSIna_2kXu9MegIvc0pzrCoGis4U/edit?usp=sharing
class EmployeeList:

    raiseAmount = 2.5

    def __init__(self, first, last, pay):
        self.firstname = first
        self.last = last
        self.pay = pay
        self.__email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.firstname, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

#class methods and static methods

    @classmethod #class method literally changes the first argument from self to a class
    def set_raise_amt(cls, amount): #can't use the word 'class' as it has a different logical operations within Python
        cls.raiseAmount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            
#Note: In python dates have weekday methods where monday = 0
# and sunday = 6 and all the ones in between  etc.
            return False
        return True

#Getter & Setter methods"""

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

# print(employeeOne.firstname)
# print('{} {}'.format(employeeOne.firstname, employeeOne.last))
# this is a very long winded way to do a class-method
#this should print out the employees first and last name

# {} {} #are just place holders which when run will output e.g. first and last name of specified employee"""

#print(employeeOne.fullname()) # make sure you use the '()' as it is a METHOD
# print(employeeTwo.fullname())
#EmployeeList.fullname(employeeTwo) #makes it easier link I think # this way you have to specify the instance
#can also use methods using the class name

"""Class Variables"""

class Espresso:
    menu_type = "Drink"
espresso_order = Espresso()
print(espresso_order.menu_type)
#output should be 'Drink' #Here we declared the instance of the class

"""Because the class variable is associated with a class, 
we don’t  need to declare an instance of our class to see its value."""

class EspressoNew:
	menu_type = "Drink"
#The following code allows us to see the value of our menu_type class variable:
print(EspressoNew.menu_type)
#The following code allows us to see the value of our menu_type class variable:
#Here we use the dot notation to access the value of the menu_type variable in our EspressoNew class.
#Here we do not declare an instance of our class.

#Class variables can be called via the instance of a specified instance. if the latter it will check if
#the attribute has the parameter if not it will check if the class it inherits from done , which is our class variable

"""Decorators"""

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
decorate()

#This is the best way to apply a Decorator
@uppercase_decorator #Using the @ symbol
def say_hi():
    return 'hello there'
say_hi()

employee3 = EmployeeList('James', 'Statt', 88000)
employee4 = EmployeeList('Stev', 'Bevver', 1400)
print('check below')
employee3.setEmail('hj@gmail.com')
print(employee3.getEmail())
EmployeeList.set_raise_amt(4) # doing this is the equivalent to see one line below
EmployeeList.raiseAmount = 7 # same as line 100 but without using a 'class-method'
#You can run the classmethod using the instance to get the same result but it doesnt makes sense to do so


"""Using class-methods as alternative constructors"""

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay) 116 and 117 are very long winded
# if this is how all the data is presented(in strings here)
new_emp_1 = EmployeeList.from_string(emp_str_1) #using the classmethod

import datetime
my_date = datetime.date(2016, 7, 11)
print(EmployeeList.is_workday(my_date))

"""Subclasses"""

class Developer(EmployeeList):

    def __init__(self, first, last, pay, studentID):
        self.firstname = first
        self.last = last
        self.pay = pay
        self.ID = studentID

e_1 = EmployeeList('Knee', 'cap', 50000)
#It will check our developer class FIRST for our __init__
# but its empty so it will walk up the chain of inheritance KNWON AS the method resolution order
e_2 = EmployeeList('Test', 'Employee', 60800)
dev_3 = Developer('tester', 'idk', 5500, '2323LL')


# employeeOne.setEmail('bob@gmail.com')
