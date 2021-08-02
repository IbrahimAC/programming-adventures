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
    print(luckyList)
    print('-------------')
    for number in luckyList: #3
        print(number, 'raw num')
        if '6' == True and '8' == True in str(number):
            print(str(number), 'string num')
            luckyList.remove(number)
            print(luckyList)
    print(luckyList)
    for number in luckyList: #4
        if '8' in str(number):
            luckyCount += 1
        elif '6' in str(number):
            luckyCount +=1
    return luckyCount #5

print(luckyNumber(679,690))