# case 1
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
    print(i)

# case 2
for i in range(10):  # 0 to ni-1
    print("range", i)

# case 3
for i in range(10, 100):  # Include start and exclude end
    print(i)

# case even number
num = int(input("Enter number:"))
if (num % 2 == 0):
    print("Even")
else:
    print("Odd")
## find all even number between 100 to 100
for n in range(10, 100):
    if n % 2 == 0:
        print(n)

## Break, continue, while

i = 0
while i != 20:
    i = i + 1
    if (i % 2) == 0:
        continue
    if i == 15:
        break
    print("Odd number", i)


