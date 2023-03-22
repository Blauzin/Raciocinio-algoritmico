def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
keyMoeda = int(input("""Digite o número correspondente a moeda:
1.Dólares
2.Libras
3.Euros
"""))
valor =  float(input("Digite o valor que será adquirido da moeda: "))

dictConvert = {1:valor * 5.24, 2:valor * 6.43, 3:valor * 5.66}

if dictConvert[keyMoeda] < 1000:
    tax = 0.05
else:
    tax = 0.03

print(f"Você precisa de R$ {(dictConvert[keyMoeda] + dictConvert[keyMoeda] * tax):.2f}")