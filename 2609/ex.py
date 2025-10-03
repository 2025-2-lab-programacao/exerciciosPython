from random import randint
from typing import List

def preencheMatriz(lin: int, col: int) -> List[List[int]]:
    m = [[int(randint(0, 5)) for j in range(col)] for i in range(lin)]
    return m

def imprimeMatriz(mat: List[List[int]]) -> None:
    for linha in mat:
        print(linha)
        
def calcularElemento(a: List[List[int]], b: List[List[int]], i, j) -> int:
    x = 0
    for z in range(len(a[0])):
        x += a[i][z] * b[z][j] #fixa a linha do A e a coluna do B
    return x


def multiplicacao(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:   
    m = []
    for i in range(len(a)):
        submat = []
        for j in range(len(b[0])):
            x = calcularElemento(a, b, i, j)
            submat.append(x)
        m.append(submat)
    return m

def main() -> None:
    m1 = preencheMatriz(3, 2)
    m2 = preencheMatriz(2, 3)
    imprimeMatriz(m1)
    print(f"é")
    imprimeMatriz(m2)
    print(f"o resultado é:")
    imprimeMatriz(multiplicacao(m1, m2))
    
if __name__ == "__main__":
    main()
    