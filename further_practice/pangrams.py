#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
#Ignore numbers and punctuation.

#a pangram is a sentence, that uses every single letter of the alphabet

def is_pangram(s):

    ''' Returns true if string is a pangram
        input: string
        output: True or False (a boolean value)'''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for j in alphabet:
        if j not in pangram:
            return False
    return True
    
pangram = "The quick brown, fox jumps over the lazy dog!"
print(is_pangram(pangram))


#create a variabe containing the whole alphabet called alpahbet
#create an if statement that will compare the string against the alphabet variable
#travese the string checking each i
#see if each i is in the alphabet variable --- but we need to ignore numbers and punctuation which are all still technically i's
#if yes then return true
#create an else statement that returns false if condition isnt met
