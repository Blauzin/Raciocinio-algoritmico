inputNumbsList = []
inputNumb = 0

while inputNumb != -1:
    inputNumb = int(input("Digite um número (-1 para encerrar): "))
    inputNumbsList.append(inputNumb)

inputNumbsList.remove(-1)

sumlist = sum(inputNumbsList)
evenNumbs = []
oddNumbs = []

for number in inputNumbsList:
    if number % 2 == 0:
        evenNumbs.append(number)
    else:
        oddNumbs.append(number)
print(f"""A soma dos números digitados é: {sumlist}
A soma dos números pares é: {sum(evenNumbs)}
A soma dos números ímpares é: {sum(evenNumbs)}
A amplitude amostral é: {max(inputNumbsList) - min(inputNumbsList)}

""")