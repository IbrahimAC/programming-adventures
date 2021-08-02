
def luckyNumber(l,h):
    
    luckyCount = 0
    luckyList = []
    luckyNumbers = [6, 8]
    luckyRange = range(l,h+1) #1
    print(str(luckyNumbers[1]))
    
    for number in luckyRange: #2
        luckyList.append(number)
    print(luckyList)
    for number in luckyList: #3
        numberList = str(number)
        for n in luckyNumbers:
            if str(n) in numberList:
                if str(luckyNumbers[1]) in numberList:
                    luckyList.remove(numberList)
                elif str(luckyNumbers[1]) in numberList == False:
                    return False
    
    print(number)

    for number in luckyList: #4
        if '8' in str(number):
            luckyCount += 1
        elif '6' in str(number):
    #         luckyCount +=1


    return luckyCount #5

print(luckyNumber(65,80))
# WHAT I NEED TO DO:
# need to use a function to check if 6 or 8 and the 6 and 8 together are in the number. if so append or dont append to final list. then just do len() of said list to give amount of lucky numbers

# FUNCTION EXPLAINED
# 1 Used the range function to get a list of all the numbers inbetween and including the two given numbers
# 2 Used a For loop to append all the numbers within the range and including the given numbers into a list
# 3 Used a For Loop to traverse my list and if said number (being compared as strings) contained both lucky numbers,the number was removed from my list
# for my #3 and #4(my 2nd and 3rd For loops) i used the str() as you cannnot iterate through the int class type
# 4 Used a For loop to check whether the remaining numbers contained '8' or '6' and if so add 1 to my lucky number counter named luckyCount
# 5 returns the amount of lucky numbers
