# Write a function which returns the same words between 2 arrays storing fruits.
# In the list storing the similarities return the longest fruit and shortest fruit

listoffruits = ["Cherry", "Mango", "Apple", "Peach", "Grapefruit", "Guava", "Banana", "Plum", "Grape", "Orange",
                "Lemon", "Jackfruit"]
listoffruits2 = ["Blackberries", "Grapefruit", "Guava", "Mango", "Kiwi", "Orange", "Pineapple", "Plum", "Raspberries",
                 "Melon", "Cherry"]


def same_fruit(any, any2): 
    newlist = [] 
    maxlen = -1  
    minlen = 10

    for i in any:
        if i in any and any2: 
            newlist.append(i) 

    for k in newlist:
        if len(k) > maxlen:
            maxlen = len(k) 
            largest = k 
    

    for n in newlist: 
        if len(n) < minlen:
            minlen = len(n)
            smallest = n

    return largest, smallest, newlist
 
print(same_fruit(listoffruits, listoffruits2))

# traverse the first list
# traverse the second list
# find fruit that are in both lists
# append those said fruit into new list
# find out the character length of each fruit in the new list
# using those given numbers (e.g. 3 and 7) print said fruit if it is <4
# print said fruit >6

