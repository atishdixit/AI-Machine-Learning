import sys
import math


my_age =100
my_name = "Atish dixit"

print("Hello", my_age, my_name)
str_01 = "\"Helloe\""
## Three type of number type
# intergers, float, complax number

# Connects
'''
Hello this multiline comments
'''

print(sys.maxsize)
print(sys.float_info.max)
print(sys.path)
print(sys.int_info)

print("type", type(int(3.6)))
f=2.463845678
print("float", type(f))
print(int(2.4))
print(type(chr(97)))
print(type(str(2.3)))

str_02 = "10"
str_03 = "20"
print("hello", int(str_02)+int(str_03))

name = input("Enter the name: ")
print(name)


num_001, num_002 = input("Enter 2 values").split()
num_001 = int(num_001)
num_002 = int(num_002)
Addition = num_001+num_002
subtraction = num_001-num_002
multiplication = num_001*num_002
division = num_001/num_002
modular = num_001 % num_002



print("{} + {} = {}".format(num_001, num_002, Addition))
print("{} - {} = {}".format(num_001, num_002, subtraction))
print("{} * {} = {}".format(num_001, num_002, multiplication))
print("{} / {} = {}".format(num_001, num_002, division))
print("{} % {} = {}".format(num_001, num_002, modular))



miles = input("Please enter miles want to convert in to KM")
factor = 1.60934;
km = int(miles) * factor
print("{} miles equals {} kilometers ".format(miles, km))

print(math.pow(2,10))
print(math.log(2, 10))
print(math.factorial(5))
print(math.trunc(2.2))
print(math.ceil(4.4))
print(math.floor(4.6))


