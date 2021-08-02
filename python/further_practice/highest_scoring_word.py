
#Attempt 1
def high(x):

    '''Returns the highest scoring word
      input: a string
      output: string (the highest scoring string)'''
  
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    storenum = [] #Stores the score of each letter per word.
    findme = x #input string
    splitString = findme.split() #Splits string into array of strings
    print(splitString[0])

    for y in alphabet: #loop through alphabet
        for j in x: #lopp through input string
            if y == j: #Check if the letter in the alphabet is the same as the letter in input string
                storenum.append(alphabet.index(y) + 1) #Gets score.

    return storenum


print(high('Welcome to Australia'))