precoProduto =  float(input("Digite o preço do produto: "))

keyOpt = int(input("""Digite o número em relação a opção desejada:
1. À vista com 8% de desconto.
2. Parcelado 2 vezes com 4% de desconto.
3. Parcelado em 3 vezes se qualquer tipo de desconto.
4. Parcelado em 4 vezes com 4% de acréscimo.
"""))

# keyOpt pega um número do usuário equivalente a opção de pagamento preferida que será correlacionado a uma conta no dictPay

dictPay = { 1:precoProduto - precoProduto*0.08, 2:(precoProduto - precoProduto*0.04)/2, 3: precoProduto/3, 4:(precoProduto + precoProduto*0.04)/4}
dictPayText = {1:f"O pagamento será em 1 parcela de R$ {dictPay[keyOpt]:.2f}.", 2:f"O pagamento será 2 parcelas de R$ {dictPay[keyOpt]:.2f}.",3:f"O pagamento será em 3 parcelas de R$ {dictPay[keyOpt]:.2f}.", 4:f"O pagamento será realizado em 4 parcelas de R$ {dictPay[keyOpt]:.2f}." }
#dictpayText relaciona a chave do usuário de keyopt com o texto que deve ser printado ao final, economizando linhas.

print(dictPayText[keyOpt])