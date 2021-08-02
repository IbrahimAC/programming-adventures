#Task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

def order(sentence):

    """Returns a sorted string, using the number in the word as its position in the 'ordered' sentence
       input: a string
       output a string"""

    s = sentence.split()
    orderedSentence = []
    checker = 1

    while checker <= len(s):
        for l in s:
            current = l.count(str(checker))

            if current == 1:
                orderedSentence.append(l)
        checker += 1

    return ' '.join(orderedSentence)

print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order("1get w4eek fi2nd be3 a5t"))