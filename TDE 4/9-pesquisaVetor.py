contador = 0
vLido = []

while contador < 10:
    intInput = int(input("Digite um número a ser adicionado ao espaço amostral: "))
    vLido.append(intInput)
    contador += 1

numSearch = int(input("Digite um número a ser pesquisado: "))

if numSearch in vLido:
    indices = [i for i, x in enumerate(vLido) if x == numSearch]
    print(f"O número foi encontrado {vLido.count(numSearch)} vezes, nos indexes {indices}")
