matriz = [[1,2,3], [4,5,6], [7,8,9]]
def printMatriz():
    for i in range(len(matriz)):
        print(matriz[i])

printMatriz()
numeroMultiplicador = int(input("Digite um número para multiplicar a matriz acima: "))


def multiplicarMatriz(matriz, numeroMultiplicador):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
                matriz[linha][coluna] =  matriz[linha][coluna] * numeroMultiplicador   
        
multiplicarMatriz(matriz, numeroMultiplicador)
printMatriz()
