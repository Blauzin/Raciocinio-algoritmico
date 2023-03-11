valorProduto = float(input("Digite o valor do produto: "))

print("O valor a vista é: R$ " + str(round(valorProduto - (valorProduto * 0.05), 2)) + ", o valor da parcela  em 2 vezes é R$ " + str(round(valorProduto / 2, 2)) + ", o valor parcela em três vezes é: R$ " + str(round((valorProduto + valorProduto * 0.05 / 3), 2)))
#calcula todos os valores e arredonda para duas casas decimais diretamente no print
