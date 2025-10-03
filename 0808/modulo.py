# funcao para calcular o total de grãos
def calcular(a: int, b: int) -> int:
    total = 0
    for i in range(64):
        total += 2**1
    return total

#programa principal
total = calcular()
print(f"total de grãos: {total}")
print()