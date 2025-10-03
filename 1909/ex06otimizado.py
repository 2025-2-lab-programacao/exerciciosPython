from random import randint
from typing import List, Tuple

def preencheMatriz(row: int, column: int) -> List[List[int]]:
    return [[randint(-10, 40) for _ in range(column)] for _ in range(row)]

def imprimeMatriz(mat: List[List[int]]) -> None:
    for linha in mat:
        print(linha)

def mediasPorAno(mat: List[List[int]]) -> List[float]:
    return [sum(linha) / len(linha) for linha in mat]

def minMaxMedia(medias: List[float]) -> Tuple[int, float, int, float]:
    maxId = max(range(len(medias)), key=lambda i: medias[i])
    minId = min(range(len(medias)), key=lambda i: medias[i])
    return (maxId, medias[maxId], minId, medias[minId])

def main() -> None:
    matriz = preencheMatriz(10, 12)
    imprimeMatriz(matriz)
    
    medias = mediasPorAno(matriz)
    for i, m in enumerate(medias, start=1):
        print(f"A média do {i}° ano é {m:.2f}")
    
    maxId, maxValor, minId, minValor = minMaxMedia(medias)
    print(f"\nAno com maior média: {maxId+1}° ({maxValor:.2f})")
    print(f"Ano com menor média: {minId+1}° ({minValor:.2f})")

if __name__ == "__main__":
    main()