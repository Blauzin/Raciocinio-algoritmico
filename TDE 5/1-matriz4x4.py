
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
            element = int(input(f"Insira o elemento na posição ({i+1}, {j+1}): "))
            linha.append(element)
    matriz.append(linha)

listaMaiores = []

for i in range(4):
      listaMaiores.append(max(matriz[i]))
print(listaMaiores)