num_01, operation, num_02 = input("Eneter expression like 2+3, 2*8 ").split()
resut = 0
if(operation == "+"):
    resut = (int(num_01) + int(num_02))
elif (operation == "-"):
    resut = (int(num_01) - int(num_02))
elif (operation =="*"):
    resut = (int(num_01) * int(num_02))
elif (operation == "/"):
    resut = (int(num_01) / int(num_02))
else:
    resut = 0;

print("{} {} {} = {}".format(num_01, operation, num_02, resut))

age = int(input("Enter age "))

if(age<10):
    print("Chhotu")
elif(age> 10 and age<=20):
    print("badkau")
elif not age == 80 or age ==90:
    print("ok ok")

age = int(input("Enter age again for vote"))
can_vote = True

