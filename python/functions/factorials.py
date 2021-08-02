#Creating a factorial function

def factorial(n):

#This is an iterative approach

    """Returns the factorial of the given integer
       input: int
       output int"""

    base = 1

    for i in range(1,n+1):

        base = i * base
    return base

print(factorial(3))

#Example case by case function breakdown:

#1 , base = 1x1
#2, base = 1x1x2
#3, base = 1x1x2x3