#This is a beginner python exam I did to test my knowledge 
#exam 14/03/2021 23:36

#This dictionary a key to help better understand the rest of the file
keyForExam = {
    'WRONG' : 'My answer was wrong',
    'CORRECT' : 'My answer was correct',
    'Output' : 'What would show in the output'
}


"""problem 1, what is the output?"""

valueOne = 5 ** 2
valueTwo = 5 ** 3

print(valueOne)
print(valueTwo)

#Output: 25
#Output: 125

#CORRECT


"""problem 2, what is the output?"""

var = "James" * 2  * 3
print(var)

#My answer: assumed you could not multiply a 'string' by a int or a float without converting it to said thing

#Output: JamesJamesJamesJamesJamesJames
#WRONG 



"""problem 3, what is the output?"""

var1 = 1
var2 = 2
var3 = "3"
# print(var1 + var2 + var3)

#Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

#WRONG
#cannot combine strings and ints


"""problem 4, what is the output?"""

a, b = 12, 5
if a + b:
    print('True')
else:
    print('False')

#Output: True

#CORRECT
#if condition is just checking if sum is logical and if so will print True


"""problem 5, what is the output?"""

x = 50
def fun1():
    x = 25
    print(x)
fun1()
print(x) 

#Output: 25
#Output: 50

#CORRECT
#x only prints twice, once for when the function is called and once for the print statement


"""problem 6, what is the output?"""

print(type(10))

#Output: <class 'int'>

#CORRECT

"""problem 7, what is the output?"""

print(type([]) is list)

#Output: True

#CORRECT


"""problem 8, what is the output?"""

def func1():
    x = 50
    return x
func1()
print(x)

#My Answer: x is undefined will be an error

#Output: 50
#WRONG


"""problem 9, what is the output?"""

x = 0
a = 5
b = 5

if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

#Output: x is 3

#CORRECT


"""problem 10, what is the output?"""

x = 0
while (x < 100):
  x = x + 2
print(x)

#Output: 100

#WRONG .5 on the board


"""problem 11, what is the output?"""

salary = 8000

def printSalary():
    salary = 12000
    print("Salary:", salary)

printSalary()
print("Salary:", salary)

#Output: Salary: 12000, Salary: 8000
#WRONG

"""problem 12, what is the output?"""

numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
    for y in items:
        y = y
print(x, y) 

#My Answer: print is double indented so it might print 10,chair table. 10,chair, table, 2o chair, table
#Output: 20 Tabe
#WRONG