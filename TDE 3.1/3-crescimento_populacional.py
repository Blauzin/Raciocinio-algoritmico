populacao1 = 80000
populacao2 = 200000
years = 0


while populacao1 <= populacao2:
    populacao1 = populacao1 + populacao1*0.03
    populacao2 = populacao2 + populacao2* 0.015
    years += 1

print(f"""" população 1: {populacao1:.0f}
população 2: {populacao2:.0f}
tempo: {years}
""")