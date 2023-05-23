
#entrada de dados: minutos no estacionamento
minutos = int(input("Digite quantos minutos você utilizou o estacionamento: "))

if minutos >= 75:
    preço = 8 + int((minutos - 60)/15) * 1.50
    print("Valor fracionado, R$ ", preço)
else:
    print("Valor mínimo, R$ 8.00")