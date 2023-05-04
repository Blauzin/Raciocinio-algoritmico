import sys
contador = 0
vLido = []
vTemp = []
vNew = []
while contador < 10:
    intInput = int(input("Digite um número a ser adicionado ao espaço amostral: "))
    if intInput < 0:
        print("Número Inválido, repita o processo.")
        sys.exit()
    vLido.append(intInput)
    contador += 1
for numb in vLido:
    if numb % 2 == 0:
        vNew.append(numb)
    else:
        vTemp.append(numb)
for i in vTemp:
    vNew.append(i)


print(vLido)
print(vNew)