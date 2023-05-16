import random

numSorteados = random.sample(range(10, 100), 25)
count = 0
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
            linha.append(numSorteados[count])
            count += 1
    matriz.append(linha)

def printMatriz():
    for i in range(len(matriz)):
        print(matriz[i])

printMatriz()
print("----------------")



def cruz(matriz):
    soma = 0
    for linha in range(5):
        for coluna in range(5):
                if linha != 2 and coluna != 2: 
                    matriz[linha][coluna] = " "
                else:
                     soma +=  matriz[linha][coluna]
    return soma
#soma = cruz(matriz)

#printMatriz()
#print(soma)

def cubo(matriz):
    soma = 0
    for linha in range(5):
        for coluna in range(5):
                if linha not in (0,4) and coluna not in (0,4) : #not inverte o valor de in que verifica se o valor se encontra na lista
                    matriz[linha][coluna] = " "
                else:
                    soma +=  matriz[linha][coluna]
    return soma

 
#soma = cubo(matriz)
#printMatriz()
#print(soma)

def doubleLines(matriz):
    soma = 0
    numX = 0
    numY = -1
    for linha in range(5):
        numX += 1
        numY += 1
        for coluna in range(5): #são necessários dois Ifs pois par "espelhado" se encontra na linha seguinte 
            #ou seja, 0,1 está na linha 0 mas 1,0 está na lina 1 então quando o verificador está vendo a linha 1 ele precisa voltar pra ver o espelho do X e Y anterior
            if (coluna == numX and linha == numY) or (coluna == numY - 1 and linha == numX - 1):
                  soma +=  matriz[linha][coluna]
            else:
                matriz[linha][coluna] = " "


    return soma
soma = doubleLines(matriz)
printMatriz()
print(soma)


def xadrez(matriz):
    soma = 0
    for linha in range(5):
        for coluna in range(5):
            if (linha + coluna) % 2 == 0:
                matriz[linha][coluna] = " "
            else:
                soma +=  matriz[linha][coluna]
    return soma

#soma = xadrez(matriz)
#printMatriz()
#print(soma)