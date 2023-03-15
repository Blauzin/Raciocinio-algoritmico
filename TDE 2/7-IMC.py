#calculador IMC

#entrada de dados
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if 18.5 <= imc < 25: #peso dentro do ideal