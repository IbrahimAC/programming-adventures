
#Attempt 1
def remove_duplicate_words(s):

    half = s.split()
    uw = []

    for i in half:
        checker = i
        if i == i:
            uw.append(i)

    return uw
    #return ' '.join(unique_word)

print(remove_duplicate_words("my cat is my cat fat"))