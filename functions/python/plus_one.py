def plusOne(n):

    """ Returns the array with each integer increased by 1
        input: an array
        output: an array"""

    for i in range(0,len(n)):
        n[i] = n[i] +1
    return n

print(plusOne([1, 2, 4, 5, 7]))

# test = [1, 2, 4, 5, 7]
# test[3] = 1000
# print(test)