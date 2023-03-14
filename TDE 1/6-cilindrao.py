import math 
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

area = (2 * math.pi * raio * (raio + altura)) + (2 * math.pi * (raio ** 2))
latas = (area / 3)/5

print(f"Você vai precisar de {math.ceil(latas)} latas de tinta para pintar o cilindro e custará R$ {latas * 50:.2f} reais.")