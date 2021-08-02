# Challenge change the name of the good fruit to the name of the longest trash fruit.
#A trash fruit is any fruit longer than 5 letters

newlistoffruits = ["Cherry", "Mango", "Apple", "Peach", "Banana", "Plum", "Grape", "Lemon", "Jackfruit"]

#Attempt 1
def moreTrashFruit(fruit):

    """ Returns an array where any word less than 5 letters has been replaced with the longest word that is above 5 letters
        input: an array
        output: an array"""

    betterlistoffruits = newlistoffruits
    i =  newlistoffruits[0] in newlistoffruits

    # while i in newlistoffruits != 'trash':
    #     i = 'Jackfruit'
    # return newlistoffruits
    print(i, 'iii')
    while i > 6 :
        for i in range(len(newlistoffruits)):
            print(i)
            i = 'trash'
        
    return'hi'

print(moreTrashFruit(newlistoffruits))

