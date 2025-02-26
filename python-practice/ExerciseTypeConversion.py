import datetime
# Exercise Type Conversion
# Write a program which tells your age


birth_year = input('What year were you born?\n')
today = datetime.date.today()
year = today.year
age = year - int(birth_year)
print(f'Your age is {age} years.')