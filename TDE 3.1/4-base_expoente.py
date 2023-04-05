base = int(input("Digite um número para a base: "))
expoente = int(input("Digite um número para o expoente: "))


while expoente > 0:
    resultado = base * base
    expoente -= 1

print(resultado)
