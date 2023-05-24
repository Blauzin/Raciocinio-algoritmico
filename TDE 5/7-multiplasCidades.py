#matriz que contem as distancias entre as cidades
matrizDistancias = [[0, 310, 716, 408, 852],
                    [310, 0, 470, 705, 1144],
                    [716, 470, 0, 1119, 1533],
                    [408, 705, 1119, 0, 429],
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
#cria uma lista com a sequência das cidades e pega velocidade da viagem
listaCidades = []
cidade = input("Digite a cidade inicial: ")
listaCidades.append(cidade)
while cidade != "pare":
    cidade = input("Digite a próxima cidade ('pare' para parar):")
    listaCidades.append(cidade)
listaCidades.pop()

soma = 0    
i = 0
for i in (range(len(listaCidades) - 1)):
        distancia = matrizDistancias[dictCidades[listaCidades[i + 1] ]] [dictCidades[listaCidades[i]]]
        print(f"{listaCidades[i]} >>>> {distancia}Km >>>>{listaCidades[i + 1 ]} ")
        print(" ")
        soma += distancia
        i += 1
print(f"Distância total: {soma} KM")
