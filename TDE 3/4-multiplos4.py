num = 1
result = [1]
while num*4 <= 100:
    result.append(num*4)
    num += 1
print(result)
#como o valor inicial é definido em 1 apenas multiplicar por 4 já resulta nos múltiplos de 4. 1 está incluso no result uma vez que 1 sempre é múltiplo

'''pode ser feito assim também:
result2 = [1]
for number in range(1,101):
    if number % 4 == 0:
        result2.append(number)
print(result2)
'''