#Análise de Temperaturas Médias Anuais: Você foi contratado para realizar uma análise
#simples das temperaturas médias anuais de uma cidade ao longo dos últimos 10 anos. Os
#dados são fornecidos em um formato de matriz (array bidimensional), onde cada linha
#representa um ano e cada coluna representa um mês (de janeiro a dezembro).
#Instruções:

#a) Crie uma matriz de 10x12 contendo as temperaturas médias mensais de cada ano (valores
#fictícios podem ser utilizados para testar o código).

#b) Escreva uma função que calcule a média de cada linha (ano) e retorne uma lista com as
#médias.

#c) Escreva outra função que determine o ano com a maior média e o ano com a menor média.

#d) Implemente um programa principal que utilize essas funções para processar os dados e
#imprimir os resultados

from random import randint
from typing import List

def preencheMatriz(row: int, column: int) -> List[List[int]]:
    m = [[int(randint(-10, 40)) for j in range(column)] for i in range(row)]
    return m

def imprimeMatriz(mat: List[List[int]]) -> None:
    for linha in mat:
        print(linha)
        
def mediaAno(mat: List[List[int]], med: List[List[int]]) -> None:
    for i in range(len(mat)):
        soma = 0
        for j in range(len(mat[i])):
            soma += mat[i][j]
        med.append(soma/len(mat[i]))
        print(f"A média do {i+1}° ano é {med[i]:.2f}")
        
def minMaxMedias(med: List[int]) -> None:
    mai = 0
    men = 0
    for i in range(len(med)):
        if i == 0: mai, men = i, i
        if(med[mai]<med[i]): mai = i
        if(med[men]>med[i]): men = i
        
    print(f"O ano com maior média é o {mai+1}° de média {med[mai]:.2f}\nO ano com menor média é o {men+1} de média {med[men]}")
        
                     
def main() -> None:
    matriz = preencheMatriz(10,12)
    imprimeMatriz(matriz)
    medias = []
    mediaAno(matriz, medias)
    minMaxMedias(medias)
    
if __name__ == "__main__":
    main()
    