import math
import sys
## math.sqrt()
number = float(input("Digite um número: "))

if number <= 0:
    print("Número inválido.")
    sys.exit()

numSqr = math.sqrt(number)

print(f"A raíz quadrada do número é {numSqr}")
    

