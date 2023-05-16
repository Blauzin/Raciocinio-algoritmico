matriz = [[1,2,3], [4,5,6], [7,8,9]]
def printMatriz():
    for i in range(len(matriz)):
        print(matriz[i])

printMatriz()
numeroMultiplicador = int(input("Digite um número para multiplicar a matriz acima: "))

for linha in range(3):
      for coluna in range(3):
            matriz[linha][coluna] =  matriz[linha][coluna] * numeroMultiplicador
        

printMatriz()
