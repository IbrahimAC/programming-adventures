#checks if every single number in the parameter is even and then returns  true else returns false
def checkEven(num):
    num = str(num)

    for n in num:
        if int(n) % 2 != 0:
            return False
    
    return True


print(checkEven(86))
print(checkEven(444445))
print(checkEven(3759))
print(checkEven(8867))
print(checkEven(26))