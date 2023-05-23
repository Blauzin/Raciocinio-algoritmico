import random

def printMatriz(matriz):
    for i in range(1,105,7):
        print(matriz[i])

def listNumbsSortidos(amount):
    numSorteados = []
    for i in range(amount):
        # cria a lista de numeros sortidos a serem colocados na matriz
        numSorteados.append(random.randint(10,100))
    return numSorteados
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


numSorteados = listNumbsSortidos(105)
matriz = criarMatriz(15, 7, numSorteados)
printMatriz(matriz)