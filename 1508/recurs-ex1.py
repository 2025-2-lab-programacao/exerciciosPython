#Escreva um programa em python contendo uma função recursiva que receba como
#parâmetro uma lista contendo números inteiros e seu tamanho. A função recursiva deverá
#retornar o maior valor armazenado na lista.

from random import randint
from typing import List

#usando função python - não recursiva
def maior1(lista: List) -> int:
    return max(lista)

#lógica manual - não recursiva
def maior2(lista: List) -> int:
    maior = lista[0]
    for i in range(1, len(lista)):
        if maior < lista[i]: maior = lista[i]
    return maior
        
def maiorRecursivo(lista: List, n: int) -> int:
    if n == 1:
        return lista[0]
    
    maior_sublista = maiorRecursivo(lista, n - 1)
    
    if lista[n - 1] > maior_sublista:
        return lista[n - 1]
    else:
        return maior_sublista

def preencheLista(lista: List) -> List:
    lista = [randint(0, 100) for _ in range(len(lista))]
    return lista
    
def main() -> None:
    valores = [0] * 10
    valores = preencheLista(valores)
    print(valores)
    print(maior1(valores))
    print(maior2(valores))
    

if __name__ == "__main__":
    main()