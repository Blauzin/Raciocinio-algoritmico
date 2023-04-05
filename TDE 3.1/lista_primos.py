numb = input("Digite um número para definir o final da lista: ")

if numb > 1: 
    if numb == 2:
        print(numb)
    elif numb == 3:
        print(numb)
    for i in range(2, numb):
        if numb % i == 0:
            print(numb, "não é primo.")
            break
        else:
            print(numb, "é primo.")
            break
else:
    print(numb, "é primo.")

