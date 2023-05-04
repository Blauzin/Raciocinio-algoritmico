import random

numSorteados = random.sample(range(60), 6)
acertos = 0
numerosUser = []
contador = 0
while contador < 6:
    intInput = int(input("Digite seus números da MegaSena: "))
    numerosUser.append(intInput)
    contador += 1

for sort in numSorteados:
    for escolha in numerosUser:
        if sort == escolha:
            acertos += 1

if acertos == 6:
    print("Você ganhou parabéns! ")
else:
    print(f"Você acertou {acertos} vezes")


