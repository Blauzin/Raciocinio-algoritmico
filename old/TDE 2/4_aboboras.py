import sys
diametroAbobora =  float(input("Digite o diâmetro da abóbora: "))
if diametroAbobora <= 0:
    print("Valor inválido.")
    sys.exit()
if 15 > diametroAbobora or diametroAbobora >= 20:
    print("Produto fora das medidas.")
    sys.exit()
else:
    print("Produto de classifição média, próprio para empacotamento.")	