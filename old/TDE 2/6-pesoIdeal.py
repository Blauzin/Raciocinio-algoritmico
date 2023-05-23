altura = float(input("Digite sua altura em metros: "))
sexo =  int(input("Digite seu sexo 1 para masculino e 2 para feminino: "))

if sexo == 1:
    pesoIdeal = (72.7 * altura) - 58
elif sexo == 2:
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print("Input inválido.")

print(f"Seu peso ideal seria {pesoIdeal:.2f} KG.")