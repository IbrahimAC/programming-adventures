#given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    
    """ Returns the highest and lowest number
        input: an array
        output: two ints"""

    numbers = numbers.split()
    joe =[]
    high = []
    for i in numbers:
        z = int(i)
        joe.append(z)
    joe.sort()
    return str(joe[-1]) +' ' + str(joe[0])

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))