#Implementing and testing a Binary Sort Algorithm

def binarysort(array,element):

    beg = array[0]
    end = array [-1]
    mid = array[0] + array[-1] // 2

    if element == mid:
        return len(array) // 2

    for i in array:

        if element < mid:
            beg = array[0]
            end = mid
            mid = beg + end // 2
            return 'element is smaller'

        elif element > mid:
            beg = mid
            end = array[-1]
            mid = beg + end //2
            return 'element is larger'

print(binarysort([1,2,3,4,5,6,7,8,9,10], 4))