numeroInput =  input("digite 3 numeros: ")
numeros = numeroInput.split() 
floatNumeros = [float(num) for num in numeros]
floatNumeros.sort(reverse=True)
print(floatNumeros)