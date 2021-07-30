#Given an array of integers, find the one that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.

#Attempt 1

numberList = (1, 4, 2, 9, 7, 8, 9, 3, 1)
def find_it(seq):
    '''Returns the intger that appears an odd number of times
       input: An array of integers
       output: (int) that appears an odd number of times'''
    intcount = 0

    for n in seq:
        if seq.count(n) > intcount:
            intcount = seq.count(n)
        
        return n
        

print(find_it(numberList))



#Attempt 2
def findOdd(seq):

    '''Returns the integer that appears an odd number of times
       input: An array of integers
       output: (int) that appears an odd number of times'''
    
    oddInteger = 0

    for n in seq: 
        if seq.count(n) % 2 != 0:
            oddInteger = n
    
    return oddInteger
print(findOdd([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])) #5

#checks how many iterations of n there are in the array & if the amount is divisible by multiples of 2 are unequal to 0
#changes the value of oddInteger into the current iteration of n when the 'if' condition is met

