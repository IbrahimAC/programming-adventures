#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed.

def spin_words(sentence):
    
    """Returns a string but with all words five or more letters long reversed
       input: a string
       output: a string"""
    
    s = sentence.split()
    reversed = []
    
    for x in s:
        if len(x) >4: 
            x = x[::-1] 
            reversed.append(x)
        else:
            reversed.append(x) 
            
    return ' '.join(reversed)

print(spin_words('welcome'))
print(spin_words('Hi welcome to New Zealand!'))

# def spin_words(sentence):
#     # Your code goes here

#     flip = []
#     for i in sentence:
#         print(i)# traverse the string
#         if len(i) > 4:  # if the string is greater than 4 lettes then...
#             print(i)
#             i = i[::-1]
#             print(i) # reverse the word by rewriting it from the last index to the first
#             flip.append(i)
#     return flip  # returns the amended sentence
# spin_words('welcome')
# #exam 14/03/2021 23:36


