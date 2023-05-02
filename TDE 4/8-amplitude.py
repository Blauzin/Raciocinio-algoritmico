contador = 0
amostral = []

while contador < 10:
    intInput = int(input("Digite um número a ser adicionado ao espaço amostral: "))
    amostral.append(intInput)
    contador += 1

print(f"O maior valor no espaço amostral é {max(amostral)}, o menor é {min(amostral)} e a amplitude amostral é {max(amostral) - min(amostral)}")
