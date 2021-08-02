#Implementing and testing a Bubble Sort Algorithm

def bubblesort(arr):

    '''Returns a sorted array
       input: an array of integers
       output: an array of integers'''

    nl = []
    for i in arr:
        arr2 = arr
        for j in arr:
            print(i,'        ',j)
            if i >= j[0]:
                nl.append(i)
                arr2.remove(j[0])
    return nl
    print(arr)
    print('')
    correct = False

#Attempt 2
def bubblesortNew(arr):

    '''Returns a sorted array
       input: an array of integers
       output: an array of integers'''

    print(arr)
    print('Sorted array below')
    correct = False

    while correct == False:
        correct = True
        
        for n in arr:
            k = arr.index(n)
            if k == len(arr) -1:
                pass
            elif k != len(arr) -1:
                if n > arr[k+1]:
                    correct = False
                    arr[k+1], arr[k] = arr[k], arr[k+1]
    return arr

array = [2,4,5,1,39,7,7]
array2 = [1,4,3,8,8,5]

print(bubblesort(array))
print(bubblesortNew(array2))