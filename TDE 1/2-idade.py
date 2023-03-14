import sys
from datetime import date


day = int(input("type the day you were born: "))
month = int(input("type the month you were born: "))
year = int(input("type the year you were born: "))

age = int(date.today().year - year)

if month == date.today().month and day == date.today().day:
    print(f"Happy birthday! You are {age} years old")
    sys.exit()
if month >=date.today().month and day >date.today().day:
    age = age - 1
    
    


print(f"You are {age} years old")