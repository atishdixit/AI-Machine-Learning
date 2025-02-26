from datetime import datetime

# def sum(num1, num2):
#     def dif(num1, num2):
#         return num2-num1
#     return dif

# Rule: params, *args, default param, **wkargs
# def add_all(name, *args, value='hleeo' **kwargs):
def add_all(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total+=item
    return sum(args)+total

is_friends=False
is_good_one= False
#
# cam_message = "Hello friends" if is_friends else "Hello brother"
# print(cam_message)
#
# cam_message = "Hello rahul" if not  is_friends else "Hello brother"
# print(cam_message)

# if is_friends and is_good_one:
#     cam_message = "hello friend!! you are a good!!"
# elif is_friends and not  is_good_one:
#     cam_message = "hello friend!! but you are not a good one"
# else:
#     cam_message = "Not a friend!!"
# print(cam_message)

# find duplicate from list
# duplicalte=[]
# elements_list = [1,2,3,4,5, 6,1,3, 2,4,7,4,7,3]
# for item in elements_list:
#     if elements_list.count(item) > 1 and duplicalte.count(item) <= 0:
#         duplicalte.append(item)
#
# print(duplicalte)

#print(add_all(1,2,3,4,5, num1=5, num=10));
# Best Practices
def test()->bool:
    return True
print(test())

def list_demo(numbres: list[int])->list[int]:
    return numbres

print(list_demo([1,2,3,4,5,6]))

def numbers1(*numbers: float)->float:
    sum: float = 0.0
    for item in numbers:
        sum+=item
    return sum



print(numbers1(1,2,3,4,5))

now:datetime = datetime.now()
date = f'{now:%d.%m.%y (%H:%M:%S)}'
print(date)
# Local data
date = f'{now:%c}'
print(date)