#input do usuário
numb = int(input("Digite um número a ser testado: "))

#verifica se o número não é 1, então divide
# o número por vários númerow encontrados em sua
#metade, uma vez que o menor divisor possível 
#além de 1 seria 2
primeFlag = 1

if numb > 1: 
        for i in range(2, int(numb / 2) + 1):
            if numb % i == 0:
                primeFlag = 0
                break
        if primeFlag == 1:
            print("O número", numb,"é primo.")
        else:
            print("O número", numb,"não é primo.")
else:
     print("O número", numb,"não é primo.")
