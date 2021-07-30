#Implementing and testing a Quick Sort Algorithm

def quickSort(array):

    if len(array) <= 1:
        return array
    else:
        y = array.pop()

    low = []
    high = []

    for x in array:
        if x > y:
            high.append(x)
        else:
            low.append(x)

    return quickSort(low) + [y] + quickSort(high)

print(quickSort([1,88,33,88,899, 2, 4, 6, 5, 3]))