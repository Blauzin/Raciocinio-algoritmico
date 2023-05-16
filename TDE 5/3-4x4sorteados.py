import random

numSorteados = random.sample(range(100, 1000), 16)
count = 0
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
            linha.append(numSorteados[count])
            count += 1
    matriz.append(linha)



maiorNumero = matriz[0][0]
for linha in range(4):
    for coluna in range(4):
        if matriz[linha] [coluna] > maiorNumero:
            maiorNumero = matriz[linha] [coluna] 
            linhaMaior = linha
menorNumero = min(matriz[linhaMaior])

  

print(matriz)
print(f"O maior numero é {maiorNumero}, se econtra na linha {linhaMaior} e o menor número nessa linha é {menorNumero}")