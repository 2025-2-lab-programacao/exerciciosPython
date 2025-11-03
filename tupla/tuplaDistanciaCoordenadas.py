import math
from random import randint

qtdCoord = 3
lista_gps = [(randint(-10, 10), randint(-10, 10)) for _ in range(qtdCoord)]

print(lista_gps)

maxi = -1
mini = -1
somatoria = 0
for i in range(qtdCoord):
    dist = math.sqrt((lista_gps[i][0]**2 + lista_gps[i][1]**2))
    somatoria += dist
    if dist > maxi or maxi<0: 
        maxi = dist
    if dist < mini or mini<0:
        mini = dist
    
somatoria = somatoria / qtdCoord

print(f"A maior distância é {maxi:.2f} unidades")

print(f"A menor distância é {mini:.2f} unidades")

print(f"A média das distâncias é {somatoria:.2f} unidades")