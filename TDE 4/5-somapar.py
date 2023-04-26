contador = 0
numblist = []
resultado = 0
while contador < 4:
    num = int(input("Digite um número:"))
    numblist.append(num)
    contador += 1
for i in numblist:
    if i % 2 == 0:
        resultado += i
print(resultado)
