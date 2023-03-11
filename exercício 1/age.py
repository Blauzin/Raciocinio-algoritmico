import sys


day = int(input("type the day you were born: "))
month = int(input("type the month you were born: "))
year = int(input("type the year you were born: "))

age = int(2023 - year)

if month == 3 and day == 7:
    print(f"Happy birthday! You are {age} years old")
    sys.exit()
if month >=3 and day >7:
    age = age - 1
    
    


print(f"You are {age} years old")