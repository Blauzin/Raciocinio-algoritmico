#calculador IMC
import sys
#entrada de dados
peso = float(input("Digite seu peso em kilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
# pesoMinimo = 18.5 * altura**2 
# imcMaximo = 24.9 * altura **2

if 18.5 > imc: 
    print(f"Seu peso encontra-se abaixo do normal. A menor massa considerada normal para você seria {(18.5 * altura**2):.2f}")
elif imc > 25:
    print(f"Seu peso encontra-se acima do ideal. A maior massa considerada noral para você seria {(24.9 * altura **2):.2f}")
else:
    print("Seu peso encontra-se na faixa normal.")



