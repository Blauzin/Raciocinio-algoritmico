import sys

numeroInput =  input("digite 10 numeros: ")
numeros = numeroInput.split() 
floatNumeros = [float(num) for num in numeros]
if len(floatNumeros) != 10:
    print("Quantidade inválida de números.")
    sys.exit()
print(f"A soma é {sum(floatNumeros)} e a média é {sum(floatNumeros) / 10}")