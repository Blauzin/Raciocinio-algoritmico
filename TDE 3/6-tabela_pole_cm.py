print("Tabela de Conversão de Polegadas para Centímetros")
print("Polegadas \t Centímetros") #\t é basicamente um tab para separar os valores no print.
#for cria a variável polegada para a range 1 a 21
for polegada in range(1, 21):
    cm = polegada * 2.54
    print("{:.1f} \t\t {:.2f}".format(polegada, cm))