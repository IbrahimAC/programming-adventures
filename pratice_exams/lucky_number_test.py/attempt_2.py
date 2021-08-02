#Create a function that returns the amount of lucky numbers between and including the two given numbers (L and H)
#If a number contains 6 OR 8 it is lucky HOWEVER if it contains 6 AND 8 it is unlucky

def luckyNumber(l,h):

    ''' Returns the amount of lucky numbers between the two given numbers
        input: int, int
        output: int'''

    luckyCount = 0
    luckyList = []
    luckyRange = range(l,h+1) #1

    for number in luckyRange: #2
        luckyList.append(number)
#    for number in luckyList:  # 3
#        if '6' and '8' in str(number):
#            luckyList.remove(number)
    for number in luckyList: #3  NEW AND IMPROVED. checks for 6 first and then 8 elminating my issue before.
        if '6' in str(number):

            if '8' in str(number):
                luckyList.remove(number)
    for number in luckyList: #3  NEW AND IMPROVED. checks for 6 first and then 8 elminating my issue before.
        if '8' in str(number):

            if '6' in str(number):
                luckyList.remove(number)
    for number in luckyList:  # 3  NEW AND IMPROVED. checks for 6 first and then 8 elminating my issue before.
        if '8' in str(number):

            if '6' in str(number):
                luckyList.remove(number)
    for number in luckyList:  # 3  NEW AND IMPROVED. checks for 6 first and then 8 elminating my issue before.
        if '6' in str(number):

            if '8' in str(number):
                luckyList.remove(number)
    for number in luckyList: #4
        if '8' in str(number):
            luckyCount += 1
        elif '6' in str(number):
            luckyCount +=1
    print(luckyList)
    return luckyCount #5
print(luckyNumber(8600,8700)