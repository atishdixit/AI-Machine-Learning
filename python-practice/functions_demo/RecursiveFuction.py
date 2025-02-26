def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


def sumOfDigit(digits):
    if getLen(digits) < 1:
        return 0
    else:
        return (digits % 10) + sumOfDigit(digits // 10)


def getLen(digit):
    lenOfDigit = 0
    while digit > 0:
        lenOfDigit = lenOfDigit + 1
        digit = digit // 10
    return lenOfDigit


print(sumOfDigit(12345))
#print(factorial(5))
