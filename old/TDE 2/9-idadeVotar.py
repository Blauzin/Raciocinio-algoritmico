import sys
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
    sys.exit()

if 16 <= idade < 18 or idade > 65:
    print("Seu voto é facultativo.")
elif 18 <= idade and idade < 65:
    print (18 >= idade and idade < 65)
else:
    print("Você não pode votar.")
