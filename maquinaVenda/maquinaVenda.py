tabelaMaster = [
    ['Coca-Cola', 3.75, 0],
    ['Pepsi', 3.67, 5],
    ['Monster', 9.96, 1],
    ['Café', 1.25, 100],
    ['Redbull', 13.99, 2]

]

moedas = [
    ["Nota de 50 reais", 50, 10], #Nome, valor, estoque de notas
    ["Nota de 20 reais", 20, 10], 
    ["Nota de 10 reais", 10, 10], 
    ["Nota de 5 reais", 5, 10], 
    ["Nota de 2 reais", 2, 10], 
    ["Moeda de 1 real", 1, 10], 
    ["Moeda de 50 centavos", 0.5, 10], 
    ["Moeda de 10 centavos", 0.1, 10], 
    ["Moeda de 1 real", 0.05, 10] 


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
def escolhasPreços():
    """Função pega o input do usuário  sobre quais produtos ele quer, realiza as verificações 
    necessárias para bom funcionamento e então retorna duas listas. Uma contendo os produtos escolhidos e outra 
    contendo os valores desses produtos
    """
    preços = []
    escolhas = []
    flagEscolha = True
    while flagEscolha:
        printMaquina()
        try:
            escolha = int(input("Digite o número do produto: ")) - 1

            if escolha < 0 or escolha >= len(tabelaMaster):     #ver se ultrapassa lower ou upper limits da lista
                raise ValueError("Valor inválido, digite novamente.")
            if tabelaMaster[escolha][2] == 0:       #verificação do estoque
                print("Produto Fora de Estoque.")
            else: #se o valor é válido e tem estoque: anota a escolha e o seu preço, exibe a escolha para o usuário e prompta ele para continuar a pedir ou parar
                escolhas.append(escolha)
                escolhasPreços.append(tabelaMaster[escolha][1])
                print(f"Você escolheu {tabelaMaster[escolha][0]}")
                print(f"Preço: R$ {tabelaMaster[escolha][1]}")
                resposta = input("Deseja escolher mais um produto? y/n")
                if resposta.lower() == "n":
                    flagEscolha = False
        except ValueError:
            print("Valor inválido, digite novamente.")
    return escolhas, preços




def pagamento(escolhas, preços):
    """Função que tem por objetivo realizar o pagamento dos produtos e dar baixa no estoque.
    Tendo como argumento a lista de escolhas e a lista dos preços criadas na função de escolha."""

    totalTroco = 0  #calculo do valor total para troco
    for nota in moedas:
        totalTroco += nota[1] * nota[2]


    subtotal = sum(preços)
    pagamento = float(input("Digite o valor em dinheiro: "))

            
    if pagamento < subtotal: #verificação se o pagamento colocado é suficiente
            print("Dinheiro insuficiente. Transação cancelada.")
            
        
    elif pagamento - subtotal > totalTroco: #verificação do valor do troco condizente com o estoque
            print("Reserva para troco insuficiente. Transação cancelada.")
            

    else:
        for escolha in escolhas: #alteração do estoque apenas quando o sistema garante que o valor inserido é suficiente
            tabelaMaster[escolha][2] -= 1


def calcularTroco():
    #criar função para calcular o troco



escolhas, preços = escolhasPreços()


    




