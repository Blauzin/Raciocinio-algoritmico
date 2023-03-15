numeroCopias = int("Digite o número de cópias: ")
precoCopia = 0.25
if numeroCopias >= 100:
    precoCopia = 0.20

print(f"O preço total é R$ {precoCopia * numeroCopias:.2f}.")