#Faça um programa que leia uma quantidade indeterminada de números positivos,
#encerrando quando a entrada for -1 e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
#
inputNumbsList = []
inputNumb = 0

while inputNumb != -1:
    inputNumb = int(input("Digite um número (-1 para encerrar): "))
    inputNumbsList.append(inputNumb)

inputNumbsList.remove(-1)
items25 = 0
items50 = 0
items75 = 0
items100 = 0
for i in inputNumbsList:
    if i <= 25:
        items25 += 1
    elif i <= 50:
        items50 += 1
    elif i <= 75:
        items75 += 1
    elif i <= 100:
        items100 += 1

print(f"""
Dos números colocados 
{items25} estão entre 0 e 25
{items50} estão entre 26 e 50
{items75} estão entre 51 e 75
{items100} estão entre 76 e 100

""")
