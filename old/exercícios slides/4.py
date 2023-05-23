notas = [float(nota) for nota in input("Digite as notas separadas por espaço: ").split()]
#notas nesse caso é uma lista onde utilizamos o split para separar os valores e o float para converter para float
average = sum(notas) / len(notas)

print("A média das notas é:", average)