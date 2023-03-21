num = 1
end_num = int(input("digite o número: "))

result = []
if end_num < 0:
    while num >= end_num:
        result.append(num)
        num -= 2

else:
    while num <= end_num:
        result.append(num)
        num += 2
   
print(result)
    