import time

tabelaMaster = [
    ['Coca-Cola', 3.75, 2], #nome valor(para mostrar na maquina) e estoque
    ['Pepsi', 3.67, 5],
    ['Monster', 9.96, 1],
    ['Café', 1.25, 100],
    ['Redbull', 13.99, 2]
]

moedas = [
    ["Nota(s) de 50 reais", 5000, 10], #Nome, valor (em centavos), estoque de notas
    ["Nota(s) de 20 reais", 2000, 10], 
    ["Nota(s) de 10 reais", 1000, 10], 
    ["Nota(s) de 5 reais", 500, 10], 
    ["Nota(s) de 2 reais", 200, 10], 
    ["Moeda(s) de 1 real", 100, 10], 
    ["Moeda(s) de 50 centavos", 50, 10], 
    ["Moeda(s) de 10 centavos", 10, 10], 
    ["Moeda(s) de 5 centavos", 5, 10],
    ["Moeda(s) de 1 centavo", 1, 10]
]

def modoAdmin(flag):
    while flag: 
        print("""======== Modo Administrador ========
        0 - Voltar
        1 - Adicionar item
        2 - Editar item
        3 - Excluir item
        4 - Estoque moedas
        5 - Estoque geral""")
        opt = int(input("Insira a opção desejada: "))
        if opt == 0:
            escolhasPreços(True)
            flag = False
        elif opt == 1:
            nome = input("Insira o nome do novo produto: ")
            preco = float(input("Insira o preço do novo produto: "))
            estoque = int(input("Insira o estoque do novo produto: "))
            tabelaMaster.append([nome, preco, estoque])
            print("Novo produto adicionado com sucesso!")
        elif opt == 2:
            printMaquina()
            indice = int(input("Insira o ID do produto que deseja editar: ")) - 1
            if indice >= 1 and indice <= len(tabelaMaster):
                produto = tabelaMaster[indice]
                nome = input("Insira o novo nome do produto: ")
                preco = float(input("Insira o novo preço do produto: "))
                estoque = int(input("Insira o novo estoque do produto: "))
                produto[0] = nome
                produto[1] = preco
                produto[2] = estoque
                print("Produto editado com sucesso!")
            else:
                print("Índice inválido!")
        elif opt == 3:
            printMaquina()
            index =  (int(input("Digite o número do produto a ser deletado: ")) - 1)
            if index < 0 or index >= len(tabelaMaster):
                print("Valor inválido, digite novamente.")
            else:
                print(f"O produto {tabelaMaster[index][0]} foi excluído com sucesso!")
                tabelaMaster.pop(index)
        elif opt == 4:
            for i in range(len(moedas)):
                print(*moedas[i],)
        elif opt == 5:
            for i in range(len(tabelaMaster)):
                print(*tabelaMaster[i],)
    	    
        else:
            print("Opção inválida!")

def printMaquina():
    
    print("  ============Máquina De Vendas============")
    for n in range(len(tabelaMaster)):
        print(f"""|
|{n + 1} - {tabelaMaster[n][0]} R$ {tabelaMaster[n][1]} - estoque:({tabelaMaster[n][2]})""")
    print("========================================")


#função que pega as as escolhas e retorna o preço
def escolhasPreços(flag):
    """Função pega o input do usuário sobre quais produtos ele quer, realiza as verificações 
    necessárias para bom funcionamento e então retorna duas listas. Uma contendo os produtos escolhidos e outra 
    contendo os valores desses produtos
    """
    tempEstoque = []
    for i in range(len(tabelaMaster)):
        tempEstoque.append(tabelaMaster[i][2]) 
    #estoque temporario para o carrinho (evitar escolher mais produtos que temos)
    precos = []
    escolhas = []
    flagEscolha = flag
    while flagEscolha:
        
        printMaquina()
        try:
            escolha = int(input("Digite o número do produto: ")) - 1

            if escolha == 7574:
                modoAdmin(True)
                flagEscolha(False)

            elif escolha < 0 or escolha >= len(tabelaMaster):     #ver se ultrapassa lower ou upper limits da lista
                raise ValueError("Valor inválido, digite novamente.") #se ultrapassar gera um erro para o try
                
            elif tempEstoque[escolha] == 0:       #verificação do estoque
                print("Produto Fora de Estoque.")
                time.sleep(2) #espera antes de imprimir a maquina novamente para usuario poder ler
            else: #se o valor é válido e tem estoque: anota a escolha e o seu preço, exibe a escolha para o usuário e prompta ele para continuar a pedir ou parar
                escolhas.append(escolha)
                precos.append(int(tabelaMaster[escolha][1] * 100))
                print(f"Você escolheu {tabelaMaster[escolha][0]}")
                print(f"Subtotal: R$ {sum(precos) / 100}")
                tempEstoque[escolha] -= 1 #tira do estoque temporário
                resposta = input("Deseja escolher mais um produto? y/n ")
                if resposta.lower() == "n":
                    flagEscolha = False
        except ValueError:
            print("Valor inválido, digite novamente.")
            time.sleep(2)
    pagamento(escolhas, precos)


def calcularTroco(preço, pagamento):
    """ Função que vai pegar o valor pago e o preço, retornando o troco através das moedas e notas no estoque.
    Retorna lista com o troco e dá baixa nas moedas."""
    listaRetorno = []
    troco = pagamento - preço
    for index in range(len(moedas)): #percorrer todos os tipos de moedas
        if moedas[index][2] > 0: #verificação do estoque de moedas
            if troco >= moedas[index][1]: #se a moeda atual for menor que troco, ver quantas dela são necessárias
                numeroMoedas =  int(troco // moedas[index][1])
                if numeroMoedas > moedas[index][2]: #check para não tentar dar mais moedas que tem no estoque
                    numeroMoedas = moedas[index][2]
                troco -= (numeroMoedas * moedas[index][1]) 
                escrita = str(numeroMoedas) + " " + moedas[index][0]
                listaRetorno.append(escrita)
    return listaRetorno



def pagamento(escolhas, preços):
    """Função que tem por objetivo realizar o pagamento dos produtos e dar baixa no estoque.
    Tendo como argumento a lista de escolhas e a lista dos preços criadas na função de escolha."""

    totalTroco = 0  #calculo do valor total para troco
    for nota in range(len(moedas)):
        totalTroco += moedas[nota][1] * moedas[nota][2]


    subtotal = sum(preços)
    pagamento = int(float((input("Digite o valor em R$: "))) * 100)

            
    if pagamento < subtotal: #verificação se o pagamento colocado é suficiente
            print("Dinheiro insuficiente. Transação cancelada.")
            
        
    elif pagamento - subtotal > totalTroco: #verificação do valor do troco condizente com o estoque
            print("Reserva para troco insuficiente. Transação cancelada.")
            

    else:
        for escolha in escolhas: #alteração do estoque apenas quando o sistema garante que o valor inserido é suficiente
            tabelaMaster[escolha][2] -= 1
        if pagamento - subtotal != 0:    
            troco = calcularTroco(subtotal, pagamento)
            print("Obrigado por comprar! Segue seu troco: ")
            print(*troco, sep = ", ") #imprime a lista separada em linhas e sem o ['']
            resposta = input("Deseja escolher mais um produto? y/n ")
            if resposta.lower() == "y":
                escolhasPreços(True)

        else:
            print("Obrigado por comprar!")
            resposta = input("Deseja escolher mais um produto? y/n ")
            if resposta.lower() == "y":
                escolhasPreços(True)


escolhasPreços(True)





