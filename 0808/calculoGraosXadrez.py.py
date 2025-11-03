def calculoGraos(numQ: int):
    soma = 0
    for i in range(numQ):
        soma += 2**i
    
    return soma

        
nGraos = int(input(f"Diga o número de quadros onde os grãos serão dispostos: "))

print(f"O número de grãos é {calculoGraos(nGraos)}")