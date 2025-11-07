#Análise de Temperaturas Médias Anuais: Você foi contratado para realizar uma análise
#simples das temperaturas médias anuais de uma cidade ao longo dos últimos 10 anos. Os
#dados são fornecidos em um formato de matriz (array bidimensional), onde cada linha
#representa um ano e cada coluna representa um mês (de janeiro a dezembro).
#Instruções:

#a) Crie uma matriz de 10x12 contendo as temperaturas médias mensais de cada ano (valores
#fictícios podem ser utilizados para testar o código).

#b) Escreva uma função que calcule a média de cada linha (ano) e retorne uma lista com as
#médias. (A implementação usa uma lista passada como argumento para armazenar as médias)

#c) Escreva outra função que determine o ano com a maior média e o ano com a menor média.

#d) Implemente um programa principal que utilize essas funções para processar os dados e
#imprimir os resultados

from random import randint # Importa a função 'randint' do módulo 'random', utilizada para gerar números inteiros aleatórios.
from typing import List # Importa o tipo 'List' do módulo 'typing', usado para anotação de tipos, indicando que uma variável ou retorno é uma lista (ou lista de listas).

def preencheMatriz(row: int, column: int) -> List[List[int]]:
    # Define a função 'preencheMatriz' que recebe o número de linhas ('row') e colunas ('column').
    # Retorna uma matriz (lista de listas de inteiros). (Instrução a)


    m = [[int(randint(-10, 40)) for j in range(column)] for i in range(row)]
    # Cria a matriz 'm' usando uma 'list comprehension' aninhada:
    # - O loop externo 'for i in range(row)' itera pelas linhas (anos).
    # - O loop interno 'for j in range(column)' itera pelas colunas (meses).
    # - 'randint(-10, 40)' gera uma temperatura média inteira aleatória entre -10°C e 40°C.
    
    return m # Retorna a matriz de temperaturas preenchida.

def imprimeMatriz(mat: List[List[int]]) -> None:
    # Define a função 'imprimeMatriz' que recebe uma matriz ('mat') e não retorna nada ('-> None').
    
    for linha in mat:
        # Itera sobre cada 'linha' da matriz.
    
        print(linha)
        # Imprime a lista que representa a linha (temperaturas mensais de um ano).
        
def mediaAno(mat: List[List[int]], med: List[List[int]]) -> None:
    # Define a função 'mediaAno' que calcula a média de cada linha (ano). (Instrução b)
    # Recebe a matriz de temperaturas 'mat' e uma lista vazia/preenchível 'med' (que será preenchida com as médias).
    # Não retorna nada ('-> None'), mas modifica a lista 'med' e imprime os resultados.
    
    for i in range(len(mat)):
        # Loop para iterar sobre cada linha (ano) da matriz, usando o índice 'i'.
    
        soma = 0
        # Inicializa a variável 'soma' para acumular as temperaturas de um ano.
    
        for j in range(len(mat[i])):
            # Loop interno para iterar sobre cada elemento (mês/temperatura) na linha atual.
    
            soma += mat[i][j]
            # Soma a temperatura do mês atual à 'soma' do ano.
    
        med.append(soma/len(mat[i]))
        # Calcula a média do ano (soma dividida pelo número de meses/colunas) e a adiciona à lista 'med'.
    
        print(f"A média do {i+1}° ano é {med[i]:.2f}")
        # Imprime a média do ano atual, formatada com duas casas decimais.
        
def minMaxMedias(med: List[int]) -> None:
    # Define a função 'minMaxMedias' que encontra o ano com a maior e a menor média. (Instrução c)
    # Recebe a lista 'med' que contém as médias anuais. Não retorna nada ('-> None').
    
    mai = 0
    # Inicializa 'mai' (índice do ano com a maior média) com 0 (primeiro ano).
    
    men = 0
    # Inicializa 'men' (índice do ano com a menor média) com 0 (primeiro ano).
    
    for i in range(len(med)):
        # Itera sobre a lista de médias 'med', onde 'i' representa o índice do ano (começando em 0).
    
        if i == 0: mai, men = i, i
        # Condição de inicialização: na primeira iteração (i=0), garante que 'mai' e 'men' apontem para o primeiro elemento.
    
        if(med[mai]<med[i]): mai = i
        # Se a média atual (med[i]) for maior que a maior média registrada (med[mai]), atualiza o índice 'mai'.
    
        if(med[men]>med[i]): men = i
        # Se a média atual (med[i]) for menor que a menor média registrada (med[men]), atualiza o índice 'men'.
        
    print(f"O ano com maior média é o {mai+1}° de média {med[mai]:.2f}\nO ano com menor média é o {men+1} de média {med[men]}")
    # Imprime os resultados: o índice do ano é ajustado para começar em 1 (mai+1 e men+1).
    # A maior média é formatada para duas casas decimais.
    # A menor média é impressa.
    
def main() -> None:
    # Define a função principal 'main', que orquestra a execução do programa. (Instrução d)
    # Não retorna nada ('-> None').
    
    matriz = preencheMatriz(10,12)
    # Chama 'preencheMatriz' para criar a matriz 10x12 (10 anos x 12 meses).
    
    imprimeMatriz(matriz)
    # Imprime a matriz de temperaturas criada.
    
    medias = []
    # Inicializa a lista vazia 'medias' para armazenar as médias anuais.
    
    mediaAno(matriz, medias)
    # Chama 'mediaAno' para calcular as médias, imprimir e preencher a lista 'medias'.
    
    minMaxMedias(medias)
    # Chama 'minMaxMedias' para encontrar e imprimir o ano mais quente e o mais frio.
    
if __name__ == "__main__":
    # Bloco padrão em Python: garante que 'main()' será chamado apenas quando o script for executado diretamente.
    
    main()
    # Inicia a execução do programa.