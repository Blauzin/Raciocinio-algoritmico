from getpass import getpass
import random 
#seleção do modo
modoDeJogo =  int(input("Digite 1 para jogar contra o computador, 2 para jogar contra um amigo e 3 para uma partida entre computadores: "))

#histórico de jogos
player1score = []
player2score = []

#matriz de vitória
matrizResult = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]

#função do jogo que calcula o resultado
def jokenpoGame(hand1, hand2):
    resultado = matrizResult[hand1][hand2]
    if resultado == 0:
        print ("Empate!")
        player1score.append("empate")
        player2score.append(" empate")
    elif resultado == 1:
        
            print("Jogador 1 ganhou!")
            player1score.append("vitória")
            player2score.append("derrota")
    elif resultado == 2:
            print("Jogador 2 venceu!")
            player1score.append("derrota")
            player2score.append("vitória")

end = 0

while end == 0:
 if modoDeJogo == 1:
    #Player vs CPU
    hand1 = int(input("Escolha entre 0 - pedra, 1 - papel ou 2 - tesoura: "))
    hand2 = random.randint(0,2)
    jokenpoGame(hand1,hand2)
    end = int(input("Digite 0 para continuar e 1 para parar: "))
 elif modoDeJogo == 2:
    #Player vs Player  
    #hand1 = int(input("Jogador 1, escolha entre 1 - pedra, 2 - papel ou 3 - tesoura: "))
    #hand2 = int(input("Jogador 2, escolha entre 1 - pedra, 2 - papel ou 3 - tesoura: "))
    hand1 = int(getpass("Jogador 1, escolha entre 0 - pedra, 1 - papel ou 2 - tesoura: "))
    hand2 = int(getpass("Jogador 2, escolha entre 0 - pedra, 1 - papel ou 2 - tesoura: "))
    #getpass para não aparecer o valor no prompt de comando

    jokenpoGame(hand1, hand2)
    end = int(input("Digite 0 para continuar e 1 para parar: "))
 elif modoDeJogo == 3:
    #CPU vs CPU
    hand1 = random.randint(0,2)
    hand2 = random.randint(0,2)
    jokenpoGame(hand1, hand2)
    end = int(input("Digite 0 para continuar e 1 para parar: "))
 else:
    print("Modo de jogo inválido")
    break

if end == 1:
    print("\t     Jogador 1 \t\tJogador 2")
    n = 0
    for scores1, scores2 in zip(player1score, player2score):
        n += 1
        print("Jogo {}       {}            {}".format(n,scores1, scores2))
        #formata os resultados em uma tabela, entretando
    
