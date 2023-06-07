tabelaMaster = [
    ['Coca-Cola', 3.75, 0],
    ['Pepsi', 3.67, 5],
    ['Monster', 9.96, 1],
    ['Café', 1.25, 100],
    ['Redbull', 13.99, 2]

]

def printMaquina():
    print(f"""  ============Máquina De Vendas============
    |					   
    |1 - Coca-Cola R$ 3,75 {tabelaMaster[0][2]}
    |					   
    |2 - Pepsi R$ {tabelaMaster[1][1]} | {tabelaMaster[1][2]} Unidades(s)
    |					  
    |3 - Monster R$ {tabelaMaster[2][1]} | {tabelaMaster[2][2]} Unidade(s)
    |					  
    |4 - Café R$ {tabelaMaster[3][1]} | {tabelaMaster[3][2]} Unidades(s)
    |					  
    |5 - Redbull R$ {tabelaMaster[4][1]} | {tabelaMaster[4][2]} Unidades(s)
    |					
    |6 - Parar
    ========================================
    """)


#função que pega as as escolhas e retorna o preço
def pegarEscolhas():
    #evitar input de letras
    escolhasPreços = []
    flagEscolha = True
    while flagEscolha:  
            printMaquina()  
            try:
                escolha = int(input("Digite o número do produto: ")) - 1
            except ValueError:
                print("Valor inválido, escolha novamente.")
                escolha = int(input("Digite o número do produto: ")) - 1
            if escolha == 5:
                flagEscolha = False #para o processo

    
    if tabelaMaster[escolha][2] == 0: ##verificar estoque
        print("Produto Fora de Estoque.")
        flagEscolha = True # retornar a escolha
    elif escolha in range(5):
        print(f"Você escolheu {tabelaMaster[escolha][0]}") #printa o que vc escolheu e o preço
        print(f"Preço: R$ {tabelaMaster[escolha][1]}")
        escolhasPreços.append({tabelaMaster[escolha][1]}) #gera a lista dos preços
    
    subtotal = sum(escolhasPreços) #calcula o subtotal dos produtos

    return subtotal

#função para pagamento
def pagamento():
    try:
        valorPagamento = int(input("Digite o valor que você inseriu: "))
    except ValueError:
        print("Valor inválido, digite novamente.")
        valorPagamento = int(input("Digite o valor que você inseriu: "))





pegarEscolhas()




pagamento = pagamento()

    




