
def func1():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print(f"A soma dos números é {num1 + num2}, o produto é {num1 * num2} e i quociente é {num1 / num2}")
def func2():
    listanum = []
    num1 = listanum.append(float(input("Digite o primeiro número: ")))
    num2 = listanum.append(float(input("Digite o segundo número: ")))

    print(f"A soma dos números é {sum(listanum)}, o produto é {listanum[0] * listanum[1] } e o quociente é {listanum[0] / listanum[1] }")

func2()