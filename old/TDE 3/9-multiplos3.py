def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

limiteInicial = int(input("Digite um valor para iniciar: "))
limiteFinal =  int(input("Digite um valor final: "))
multiplos3 = []

for num in my_range(limiteInicial,limiteFinal, 1):
    if num % 3 == 0:
        multiplos3.append(num)

print(multiplos3)