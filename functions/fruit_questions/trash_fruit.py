"""Find trashfruits"""

# Go through list of fruits. Check if the fruit is trash or good.
# Trash fruits are any fruits longer than 5 letters
# Change the names of the trash fruits to "Trash" in the list.
# Return the newlistoffruits


listoffruits = ["Cherry", "Mango", "Apple", "Peach", "Banana", "Plum", "Grape", "Lemon", "Jackfruit"]
trashfruits = []

def trashFruitDetector(fruits):

    """ Returns an array where every word longer than 5 letters has been turned into the string 'trash'
        input: an array
        output: an array"""

    for x in fruits:
        if len(x) >5:
            indexstore =fruits.index(x)
            indexedfruit = fruits[indexstore].replace(x,'trash')
            trashfruits.append(indexedfruit)
        else:
            trashfruits.append(x)

    return trashfruits

print(trashFruitDetector(listoffruits))

