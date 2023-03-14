nota1, nota2, nota3, nota4 = input("Digite as notas separadas por espaço: ").split()
# pega as notas digitadas pelo usuário, separadas por espaço, e armazena em variáveis
print(f"A média das notas é {(float((nota1 + nota2 + nota3 + nota4)) / 4):.2f}")