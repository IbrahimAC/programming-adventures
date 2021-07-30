#Implementing a function that returns the count of how many letters there are in the given word

#Attempt 1
def lettercount(string):
    

    """Returns the amount of times each letter appears in a given string
       input: string
       output: lists"""
    stringlist = [] 
    lc = [] 
    for i in string:
        stringlist.append(i) 
    for i in stringlist:
        if stringlist.count(i) > 1: 

            stringlist.remove(i) 

    for i in stringlist: 
        number = string.count(i) #created a variable which stores the amount of times the given value appears in the original string
        lc.append(number) #appends the variable to our other list

    return stringlist, "occurences ->", lc #returns the list of letters and the list which contains how many times letters appear

print(lettercount('bubble'))

#list to store the individual letters
#list to store the amount of times a letter appears
#loops through the string
#appends each (i) to our new list
#loops through our list
#checks if there are any duplicate letters in our list, by checking if e.g. the amount of 'b' in our list, if greater than 1 condition is met
#created a variable which stores the amount of times the given value appears in the original string
#returns the list of letters and the list which contains how many times letters appear

#Attempt 2
def letterCount(word):

    """Returns the count of how many letters there are in the given word
       input: a string
       out: a list"""

    dict1 = { #1
        'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
        'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
    }

    for s in word:

        if s == s in dict1: #2
            dict1[s] += 1 #3

    countedLetters = [] #4

    for k,v in dict1.items(): #5

        if v >0: #6
            countedLetters.append([k,v]) #7

    return countedLetters 

print(letterCount('bubble'))

#1 - dictionary containing all of the alphabet we will compare out 'word' against
#2 -checks if s which represents the letter in the given word is equal to a key in our dictionary
#3 -if the condition is met, add 1 to the value of the corresponding key
#4 - a variable which Will store all keys and values greater than  1 to make it easier to read
#5 - loops through the dictionary which is now a tuple
#6- checks if v which represents the value in a dictionary is greater than 0
#7 - if the condition is met the appends the value and the corresponding key to our variable


#Attempt 3

def letterCountImproved(word):

    """Returns  the count of how many letters there are in the given word
       input: a string
       out: a list"""

    dictionaryOne = {}

    for letter in word:

        if letter in dictionaryOne:
            dictionaryOne[letter] +=1
        else:
            dictionaryOne.update({letter:1})

    return dictionaryOne

print(letterCountImproved('mattress'))

#this is an improved function of 'letterCount' because it is more dynamic, this is because whilst in the first function we specify a predefined Dictionary, 
#in the letterCountImproved function the keys of the dictionary are updated as we traverse the 'word' (as we go)
#this makes it more useful for situations where it is impossible to define a static Dictionary

#Creating a function that establishes whether two words are anagrams.
# an anagram is composed of the same letters , e.g. fried and fired.


def anagramDetector(word1, word2):

    word1Dict = letterCountImproved(word1)
    word2dict = letterCountImproved(word2)

    if word1Dict == word2dict:
        return True
    return False

print(anagramDetector('fried', 'fired'))
print(anagramDetector('tomato', 'potato]'))