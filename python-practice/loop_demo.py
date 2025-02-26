str='ttetgghfgjghfgfjhdfgjdhfgjhf'

def forLoopTest():
    # for item in range(5):
    #     print(item)
    # for _ in range(5):
    #     print(_)
    # for s in str:
    #     print(s)
    # for it in range(len(str)):
    #     print(str[it])
    for table in range(1, 11):
        print(table*2)

    txt = "The best things in life are free!"
    if "free" in txt:
        print("hello")

def factorial(number):
    fact = 1
    for num in range(1, number+1):
        fact = fact*num
    print(fact)
def isPrime(num):
    prime = True
    for item in range(2, num):
        if num % item == 0:
            prime = False
    return prime

def isGolden(num):
    isGolden = False
    sum_of_digit = 0
    temp_num = num
    while num > 0:
        this_num = num % 10
        num = num // 10
        sum_of_digit = sum_of_digit + pow(this_num, 3)

    if sum_of_digit == temp_num:
        print(f'number {temp_num} is golden"')
    else:
        print(f'number {temp_num} is not a golden"')


# runner
# factorial(5)
isGolden(153)