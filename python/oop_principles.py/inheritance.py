"""Inheritance"""

class Person:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def print_person(self):
        print("{} {}".format(self.name, self.lastname))

#Every person has two attributes, a first and last name.
#Every student and employee of the school will inherit the class Person

class Employee(Person):
    
    def __init__(self, name, lastname, employee_id):
        super().__init__(self, name, lastname)
        self.employee_id = employee_id

    def print_employee(self):
        print("My name is: {} {}, employee number: {}".format(self.name, self.lastname, self.employee_id))

    class Student(Person):
        def __init__(self, name, lastname, student_id):
            super().__init__(self, name, lastname)
            self.student_id = student_id

    def print_student(self):
        print("My name is: {} {}, student number: {}".format(self.name, self.lastname, self.student_id))