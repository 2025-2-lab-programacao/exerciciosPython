"""
Implemente uma função em Python que una intervalos numéricos sobrepostos.

Cada intervalo é representado por uma tupla (a, b), com a ≤ b.
A função deve receber uma lista de intervalos e retornar uma nova lista
onde os intervalos sobrepostos são fundidos.
"""


from random import randint
from typing import List, Tuple

def gerarIntervalo() -> Tuple:
    a = randint(0, 25)
    b = randint(a, 25)
    return (a,b)

def gerarListaIntervalos(qtd: int) -> List[Tuple[int, int]]:
    return [gerarIntervalo() for _ in range(qtd)]

def verificaIntervalo(int1: tuple, int2: tuple):
    inicio1, fim1 = int1
    inicio2, fim2 = int2
    
    if inicio2<=fim1 and inicio1<=fim2: 
        return (inicio1, fim2)
    else:
        return None

def atualizaIntervalos(conjInter: List[Tuple[int, int]] ):
    conjInter.sort()
    resultado = [conjInter[0]]
    
    for intervalo in conjInter[1:]:
        unido = verificaIntervalo(resultado[-1], intervalo)
        if unido:
            resultado[-1] = unido
        else:
            resultado.append(intervalo)
    return resultado
    
def main() -> None:
    a = gerarListaIntervalos(4)
    print("Intervalos gerados:", a)
    print("Intervalos unidos:", atualizaIntervalos(a))
    
    
if __name__ == "__main__":
    main()
