#calculador IMC
import sys

#entrada de dados
peso = float(input("Digite seu peso em kilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
# pesoMinimo = 18.5 * altura**2
# imcMaximo = 24.9 * altura **2


if 18.5 > imc: 
    print(f"Seu peso encontra-se abaixo do normal.")
elif imc > 30:
    print("Seu peso encontra-se na faixa de obesidade.")
elif imc > 25:
    print(f"Seu peso encontra-se acima do ideal.")
else:
    print("Seu peso encontra-se na faixa normal.")
