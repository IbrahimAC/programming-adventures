#Implementing and testing a Linear Search Algorithm

#Attempt 1
def linearSearch(array, element):
    
    """ Returns an integer that was searched for
        input: an array of ints
        output: an int """

    for n in array:
        if n == element:
            return n

    return -1 

testArray = [77,12,5,2], 12

print(linearSearch(testArray,5))
print(linearSearch([1,5,3,8,10],10))
print(linearSearch([1,5,3,8,10],99))

#Attempt 2
def linearSearch2(array, element):

    """ Returns an integer that was searched for
        input: an array of ints
        output: an int """
    
    for n in range(len(array)):
        if array[n] == element:
            return element

    return -1

#This version of the function uses the index, and checks if e.g. array[5] is equal to the specific element, if found returns it else returns -1
print(linearSearch2([1,5,3,8,10],8))
