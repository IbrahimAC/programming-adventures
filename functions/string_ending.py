
def solution(string, ending):

    """ Returns True if the 'ending' string is the same as the  equivalent part of the main string, else returns False
        input: Two strings
        output: boolean """

    endingLen = len(ending)
    stringEnd = string[-endingLen:len(string):]

    if ending == '':
        return True
    elif ending == stringEnd:
        return True
    else:
        return False


print(solution('ninja', 'ja')) 
print(solution('samurai', 'ai'))
print(solution('zebra', 'za'))
