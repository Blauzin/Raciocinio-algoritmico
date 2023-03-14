import sys
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par!")
    sys.exit()
else:
    print("O número é ímpar!")
