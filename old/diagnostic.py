loopInput = True
numPar = 0
numImpar = 0 
numPrimo = 0
while loopInput:
    numInput = int(input("Digite um numero:  "))
    if numInput < 0: 
        loopInput = False
    else:        
            if numInput % 2 == 0:
                numPar += 1
            else:
                numImpar += 1
            if numInput > 1:
                for num in range(2, int((numInput / 2) + 1)):
                    if numInput % num == 0: 
                        break
                    else:
                        numPrimo += 1
print(numPar, numImpar, numPrimo)