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
    for number in luckyList: 
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
print(luckyNumber(1,200))

