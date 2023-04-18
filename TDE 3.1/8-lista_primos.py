numb = int(input("Digite um número para definir o final da lista: "))
primeList = []


def isprime(numb):
    primeFlag = 1
    if numb > 1: 
        for i in range(2, int(numb / 2) + 1):
            if numb % i == 0:
                primeFlag = 0
                break
        if primeFlag == 1:
            primeList.append(numb)
    
    
isprime(numb)

while numb > 0:
    isprime(numb)
    numb = numb - 1
print(primeList)

    
