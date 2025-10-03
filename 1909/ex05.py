from random import randint
from typing import List

def preencheMatriz(tam: int) -> List[List[int]]:

    m = [[int(randint(0, 10)) for j in range(tam)] for i in range(tam)]
    return m

def imprimeMatriz(mat: List[List[int]]) -> None:
    for linha in mat:
        print(linha)

def trocaPosicao(mat: List[List[int]]) -> List[List[int]]:   
    cont = len(mat) - 1
    for i in range(len(mat)):
        aux = mat[i][i]
        mat[i][i] = mat[i][cont]
        mat[i][cont] = aux
        cont -= 1
        
    return mat      

def main() -> None:
    matriz = preencheMatriz(randint(2,5))
    imprimeMatriz(matriz)
    matriz = trocaPosicao(matriz)
    print("Nova Matriz")
    imprimeMatriz(matriz)
    
if __name__ == "__main__":
    main()
    