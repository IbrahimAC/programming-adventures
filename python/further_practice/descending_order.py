#A function that can take any non-negative integer as an argument and return it with its digits in descending order. 
#Essentially, rearrange the digits to create the highest possible number.

#Attempt 1
def descending_order(num):
    o = str(num)
    #o.sort()
    x = []
    x.append(o[::-1])
    res = [int(i) for i in x]

    return sum(res)
    
print(descending_order(12345))



def descending_order2(num):
    
    """Returns an integer that has been ordered from descending order
       input: int
       outut: int"""

    newList = list(str(num))
    sortedList = sorted(newList, reverse = True)
    sortedString = ''.join(sortedList)
    sortedInteger = int(sortedString)
    
    return  sortedInteger

print(descending_order2(123456789))
print(descending_order2(123333))
