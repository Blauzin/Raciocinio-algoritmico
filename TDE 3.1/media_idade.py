ageList = []
inputAge = 0
#mesmo núcleo da soma de números.
while inputAge != -1:
    inputAge = int(input("Digite uma idade (-1 para encerrar): "))
    ageList.append(inputAge)

ageList.remove(-1)
#calcula a média
média =  sum(ageList) / len(ageList)

#verifica em qual faixa a média se encontra
if média > 60:
    print("Na média são idosos.")
elif média > 26:
    print("Na média são adultos.")
else:
    print("Na média são jovens.")

print(f"{média:.2f}")