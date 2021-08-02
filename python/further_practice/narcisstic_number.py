#A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. 
# In this Kata, we will restrict ourselves to decimal (base 10).

#Attempt1
def narcissistic(value):

    stringvalue = str(value)
    lenValue = len(stringvalue)
    listvalue = list(stringvalue)
    newlist = []
    #for i in listvalue:
    [4 ** x for x in [listvalue]]

    return lenValue

#Attempt 2
def narcissisticNew( value ):

    """Returns True if a number is narcisstic, else returns False
       input: an int
       output: a boolean"""

    stringValue = str(value)
    lenValue = len(stringValue)
    listValue = list(stringValue)
    newlist = []
    
    for i in listValue:
        i = int(i) ** lenValue
        newlist.append(i)

    if (sum(newlist)) == value:
        return True

    return False
print(narcissisticNew(371))