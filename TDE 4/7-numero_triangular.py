#input do número do usuário
numero = int( \
    input("Digite um número a ser verificado: "))

prime = 1
result = 0
while result < numero:
    b = prime + 1
    c = prime + 2
    result = prime * b * c
    prime += 1

if result == numero:
    print("O número é triangular.")
    print(prime-1,b,c)
else:
    print("O número não é triangular.")
