#Implementing a function that determines whether or not a string is a palindrome
#Palindromes are words that when reversed spell the same word e.g. "kayak", "racecar"

def palindromeOne(string):

    '''Returns True if given word is a Palindrome else returns False
       input: string
       output: Boolean'''

    rstring = string[::-1] 
    if string == rstring: 
        return True
    return False 

#Relies on List Splicing
#created a string that is the reverse of original
#condition checks if the original string is equal to our new reversed string
#if condition is met returns True else it returns False

print(palindromeOne('robot'))

#Attempt 2
def palindromeA(string):

    ''' Returns True if given word is a Palindrome else returns False
        input: string
        output: Boolean'''
        
    lens = len(string)
    hl = lens //2
    string2 = []
    first = []
    second = []
    print(hl)
    for i in string:
        string2.append(i)

    for i in string2:
        if i != string2[hl]:
            print(string2[hl])
            first.append(i)
            string2.remove(i)
        elif i == string2[hl]:
            break

    return string2

#Attempt 3
def palindromeTwo(word):
    forward = []
    reversed = []
    index = len(word) -1

    for l in word:
        forward.append(l)

    while index >= 0:
        reversed.append(forward[index])
        index -= 1

    if forward == reversed:
        return True, word, 'is a palindrome'
    else:
        return False, word, 'is not a palindrome'

print(palindromeTwo('kayak'))

#Attempt 4

def palindromeImproved(word):
    firstIndex = 0
    lastIndex = len(word) -1

    while firstIndex <= lastIndex:

        if word[firstIndex]  == word[lastIndex]:
            firstIndex += 1
            lastIndex -= 1
        else:
            return False

    return True
# fi = 0 li = 4, k vs k
# fi = 1 li = 3, a vs a
# fi = 2 li = 2,  loop exited

print(palindromeImproved('kayak'))