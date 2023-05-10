def trocar_valores(lista, pos1, pos2):
    #Função auxiliar para trocar os valores de duas posições em uma lista.
    
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]

# Leitura dos números
listNumbs = []
x = 20

while len(listNumbs) < x:
    valores = input(f"Digite {x - len(listNumbs)} valores inteiros: ").split()
    for valor in valores:
        if len(listNumbs) >= x:
            break
        listNumbs.append(int(valor))

# Ordenação por seleção no vetor original
for i in range(len(listNumbs) - 1):
    indice_menor = i
    for j in range(i + 1, len(listNumbs)):
        if listNumbs[j] < listNumbs[indice_menor]:
            indice_menor = j

    trocar_valores(listNumbs, i, indice_menor)

print("Vetor ordenado:")
print(listNumbs)

