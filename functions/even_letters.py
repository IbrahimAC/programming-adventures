

def getEvenLetters(word):

    """Returns the letters at the even index
       input: a string
       output: a string"""

    even = 2
    lenL = len(word) -1
    indexs =  range(0, len(word))
    a = []

    for i in indexs:
        if i % 2 == 0:
            a.append(word[i])

    return a

print(getEvenLetters('helto'))