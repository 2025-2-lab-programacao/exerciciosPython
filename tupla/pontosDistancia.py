from math import sqrt
from random import randint

#gerar lista de pontos
# a: list[tuple]
def gerarPontos() -> list[tuple]:
    lista = []
    for _ in range(randint(1,5)):
        lista.append((randint(-10,10), randint(-10,10)))
    return lista
    
def calcularDistancia(lista):
    distancia = []
    for i in range(len(lista)):
        x, y = lista[i]
        distancia.append(sqrt(x*x + y*y))
    return distancia

def maisDistante(lista, distancia):
    ponto = lista[0]
    maior = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

def maisProximo(lista, distancia):
    ponto = lista[0]
    menor = distancia[0]
    for i in range(len(lista)):
        if distancia[i] < menor:
            menor = distancia[i]
            ponto = lista[i]
    return ponto

# funcao main()
def main():
    lista = gerarPontos()
    distancia = calcularDistancia(lista)
    print(lista)
    for i in range(len(lista)):
        print(f"{lista[i]} --> {distancia[i]}")
        
    print(f"ponto mais distante em relação a origem --> {maisDistante(lista, distancia)}")
    print(f"ponto mais proximo em relação a origem --> {maisProximo(lista, distancia)}")
    
if __name__ == '__main__':
    main()