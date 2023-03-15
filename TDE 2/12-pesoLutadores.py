
pesoKG = float(input("Digite seu peso em kilogramas: "))
pesoLibras = pesoKG * 2.20462262
print(pesoLibras)

if 161 <= pesoLibras <= 168:
    print("Sua categoria é Super-médio.")
elif 169 <= pesoLibras <= 175:
     print("Sua categoria é Meio-pesado.")
elif 176 <= pesoLibras <= 200:
     print("Sua categoria é Cruzador.")
elif 200 < pesoLibras:
     print("Sua categoria é Peso-pesado.")
else:
     print("Peso fora de categoria.")