#input do usuário
numb = int(input("Digite um número a ser testado: "))

#verifica se o número não é 1, então divide
# o número por vários número encontrados em sua
#metade, uma vez que o menor divisor possível 
#além de 1 seria 2

if numb > 1: 
    for i in range(2, int(numb / 2) + 1):
        if numb % i == 0:
            print(numb, "não é primo.")
            break
        else:
            print(numb, "é primo.")
            break
else:
    print(numb, "é primo.")

if numb == 2:
    print(numb, "é primo.")
elif numb == 3:
    print(numb, "é primo.")