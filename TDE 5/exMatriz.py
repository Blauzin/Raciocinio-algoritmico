def ex2():
    matriz = [[1,2,3], [4,5,6], [7,8,9]]
    soma = 0
    for i in range(3):
        for j in range(3):
            print(matriz[i][j])
            soma += matriz[i][j]
    print(soma)
ex2()

