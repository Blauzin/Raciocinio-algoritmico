import random

numSortidos = []

def printMatriz(matriz):
    for i in range(1,105,7):
        print(matriz[i])



for i in range(105):
    # cria a lista de numeros sortidos a serem colocados na matriz
    numSortidos.append(random.randint(10,100))

def criarMatriz(linhas, colunas, lista):
    index = 0
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(lista[index])
            index += 1
            matriz.append(linha)
    # insere a lista de números na matriz 

    return matriz

matrizOriginal = criarMatriz(15, 7, numSortidos)


print("Matriz Original:")
printMatriz(matrizOriginal) #print da matriz original


# alteração da matriz
listaPares = []
listaImpares = []
#separa em pares e impares
for number in numSortidos:
    if number % 2 == 0:
        listaPares.append(number)
    else:
        listaImpares.append(number)

for number in listaImpares: #coloca os impares ao final da lista de pares
    listaPares.append(number)

matrizFormatada = criarMatriz(15, 7, listaPares) #cria a nova matriz com a sequencia de pares - impares
print("--------------Matriz Formatada------------")
printMatriz(matrizFormatada)