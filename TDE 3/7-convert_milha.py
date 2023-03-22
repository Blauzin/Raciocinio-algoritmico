#define uma range personalizada para o for que pega um inicio, um fim e o tamanho de cada passo como variáveis.
#age de forma semelhante aos while loops nos exerícios 1 a 3.
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

print("Tabela de Conversão de Metros para Milhas")
print("Metros \t\t\t Milhas") 

for metro in my_range(20000,160000, 10000):
    milha = metro / 1609.344
    print("{:.1f} \t\t {:.2f}".format(metro, milha))