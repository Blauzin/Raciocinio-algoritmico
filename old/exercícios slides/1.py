from datetime import date
birth = input("Escreva sua data de nascimento no formato dd/mm/aaaa: ") #pega o input do usuário

day, month, year = birth.split("/") #separa a data em dia, mês e ano

age = int(date.today().year - int(year)) #calcula a idade

print("Você tem", age, "anos")
