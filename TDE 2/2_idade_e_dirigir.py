import sys
from datetime import date

birth = input("Escreva sua data de nascimento no formato dd/mm/aaaa: ") #pega o input do usuário

day, month, year = birth.split("/") #separa a data em dia, mês e ano

age = int(date.today().year - int(year)) #calcula a idade

if int(month) == date.today().month and int(day) == date.today().day:  #anivesário
    niver = "Feliz Aniversário! "
else:
    niver = ""

if int(month) >= date.today().month and int(day) > date.today().day: #subtrai um ano se a pessoa ainda nâo fez aniversário
    age =  age - 1


if age >= 18:
    canDrive = "Você já tem idade para fazer sua CNH."
else:
    canDrive = "Você não tem idade para fazer sua CNH ainda."

print(f"{niver}Você tem {age} anos de idade. {canDrive}")


