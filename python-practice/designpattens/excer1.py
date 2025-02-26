age = int(input("Enter age:"))
result = "Go to college"
if age <= 2:
    result = "Too young for School"
elif 3 <= age <= 7:
    result = "Go to Kindergarten"
elif 8 <= age < 14:
    result = "Go to Grade"

print(result)
