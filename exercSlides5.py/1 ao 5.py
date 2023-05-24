import random

def numbs100():
    listaImpares = []
    for i in range(0,200):
        if i % 2 != 0:
            listaImpares.append(i)
    print(listaImpares)
    print(len(listaImpares))

#numbs100()



def segundosDia(dias):
    quantoSegundos = dias * 24 * 60 * 60
    print(quantoSegundos)

#segundosDia(1)

def consumoCarro():
    km = float(input("Digite quantos quilômetros percorridos: "))
    litros = float(input("Digite quantos litros consumidos no trajeto: "))
    consumo = km / litros
    print(f"O consumo foi {consumo} km/l")

#consumoCarro()

vetorTeste = [1,2,3,4,5]

def dentrode(vetor, valorVerificar):
    flagDentro = False
    for i in range(len(vetor)):
        if i == valorVerificar:
            flagDentro = True

    return flagDentro

#print(dentrode(vetorTeste, 6))




def criarMatriz(linhas, colunas ):
    numSorteados = []
    amount = linhas * colunas
    for i in range(amount):
        # cria a lista de numeros sortidos a serem colocados na matriz
        numSorteados.append(random.randint(10,100))
    index = 0
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(numSorteados[index])
            index += 1
        matriz.append(linha)
    # insere a lista de números na matriz 

    return matriz

#print(criarMatriz(4,4))

