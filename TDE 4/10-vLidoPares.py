contador = 0
vLido = []
vPares = []
vImpares = []
while contador < 10:
    intInput = int(input("Digite um número a ser adicionado ao espaço amostral: "))
    vLido.append(intInput)
    contador += 1

while 0 in vLido:
    vLido.remove(0)
 
for i in vLido:
    if i % 2 == 0:
        vPares.append(i)
    else:
        vImpares.append(i)

print(vLido)
print(vPares)
print(vImpares)
