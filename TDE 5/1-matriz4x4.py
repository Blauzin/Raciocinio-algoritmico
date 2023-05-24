
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
            element = int(input(f"Insira o elemento na posição ({i+1}, {j+1}): "))
            linha.append(element)
    matriz.append(linha)



listaMaiores = []

for coluna in range(4):
    maior = matriz[coluna][coluna]
    for linha2 in range(4):
        if matriz[linha2][coluna] > maior:
            maior = matriz[linha2][coluna]
    listaMaiores.append(maior)


print(listaMaiores)