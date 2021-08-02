#Write a function that takes a string and return a new string with all vowels removed.

#Attempt 1
def disemvowel(string):

    """ Returns the given string, after removing all vowels
        input: a string
        output: a string"""

    vowels = ['a', 'e', 'i', 'o', 'u']
    clean = []
    
    for l in string:
        if l != vowels:
            clean.append(l)
    for l in clean:
        return clean

print(disemvowel("This website is for losers LOL!"))


#Attempt 2
def disemvowelNew(string):
    vowels = ['a', 'e', 'i', 'o', 'u',]
    clean = []
    
    for l in string:
        if l.lower() in vowels:
            pass
        else:
            clean.append(l)
    return ''.join(clean)

print(disemvowelNew("This website is for losers LOL!"))
