x = 20
listNumbs = []

#pede números até 20 e aceita múltiplos ao mesmo tempo
while len(listNumbs) < 20:
    listNumbsTemp  =  input(f"Digite {x} valores inteiros: ").split()
    for i in listNumbsTemp: #pega os valores a adiciona na lista correta
        listNumbs.append(int(i))
    x -= len(listNumbs)
#cleaner se a lista ultrapassar o limite
if len(listNumbs) > 20:
    while len(listNumbs) > 20:
        listNumbs.pop()
       

def trocador( lista:list , sequentialValue:int, sequentialPos:int, minValue:int, minPos:int):
    temp = sequentialValue
    lista.insert(sequentialPos, minValue)
    lista.insert(minPos, temp)


def myMin(lista:list):
    menorNumero = lista[0]
    menorNumeroPos = lista.index(lista[0])
    for pos, value in enumerate(lista):
        if menorNumero > value:
            menorNumero = value
            menorNumeropos = pos
    return menorNumero, menorNumeropos

print(listNumbs)
print(myMin(listNumbs))

