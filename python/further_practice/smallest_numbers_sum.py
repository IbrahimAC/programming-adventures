def sum_two_smallest_numbers(numbers):

    """Returns the sum of the two smallest integers
       input: an array
       output: an int"""

    numbers.sort()
    answer = ((numbers[0]) + (numbers[1]))
    return answer



def smallestSumImproved(numbers):

    """Returns the sum of the two smallest integers
       input: an array
       output: an int"""

    numbers.sort()
    return numbers[0] + numbers[1]

print(sum_two_smallest_numbers([67,5,7,12,18,22])) #12
print(smallestSumImproved([5, 8, 12, 18, 22])) #13
print(smallestSumImproved([7, 15, 12, 18, 22])) #19
print(smallestSumImproved([25, 42, 12, 18, 22])) #30