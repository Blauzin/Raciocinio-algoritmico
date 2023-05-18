#matriz que contem as distancias entre as cidades
matrizDistancias = [[0, 310, 716, 408, 852],
                    [310, 0, 470, 705, 1144],
                    [716, 470, 0, 1119, 1533], 
                    [852, 1144, 1553, 429, 0]]

#dicionario para relacionar as cidades com suas posições na matriz
dictCidades = {
    'Curitiba': 0 ,
    'Florianópolis': 1,
    'Porto Alegre': 2,
    'São Paulo': 3,
    'Rio de Janeiro': 4

}

print("""Cidades para escolha:
    Curitiba
    Florianópolis
    Porto Alegre
    São Paulo
    Rio de Janeiro

""")
#seletor de cidade e velocidade da viagem
cidadeAtual = dictCidades[input("Digite em que cidade você está: ")]
cidadeDestino = dictCidades[input("Digite qual cidade você quer ir para: ")]
velocidade = int(input("Digite a velocidade média da viagem em Km/h: "))
print(f"Você irá demorar {(matrizDistancias[cidadeAtual][cidadeDestino] / velocidade):.2f} hora(s) para chegar. ")