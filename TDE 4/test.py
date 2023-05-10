lista = [1,2,3,3,3,4,5,3,7]
x = 0
listaPos = []
valorPesquisa = int(input("Digite o valor a ser pesquisado: "))
ocorrencia = lista.index(valorPesquisa)
listaPos.append(ocorrencia)
while lista.count(valorPesquisa) > x:
    pos = lista.index(valorPesquisa, ocorrencia )
    listaPos.append(pos)
    ocorrencia = pos + 1
    x += 1

print(listaPos)