import random

def printMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def criadorMines(linhas, colunas, bombas):
    
    #criar o campo vazio
    campo = []
    for linha in range(linhas):
        linha = []
        for coluna in range(colunas):
            linha.append(" ")
        campo.append(linha)
    printMatriz(campo)
    print("----------------x-----------------")

    
    bombsPlaced = 0
    while bombsPlaced < bombas:
        linha = random.randint(0, colunas -1)
        coluna = random.randint(0, linhas - 1)
        if campo[linha] [coluna] == " ":
            campo[linha] [coluna] = "*"
            bombsPlaced += 1
        
    printMatriz(campo)

criadorMines(9, 9, 10)
