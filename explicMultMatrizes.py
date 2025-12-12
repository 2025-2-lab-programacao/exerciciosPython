from random import randint # Importa a função 'randint' do módulo 'random', usada para gerar números inteiros aleatórios.
from typing import List # Importa o tipo 'List' do módulo 'typing', usado para anotação de tipos, indicando que uma variável ou retorno é uma lista (ou lista de listas, no caso de matrizes).

def preencheMatriz(lin: int, col: int) -> List[List[int]]:
    # Define a função 'preencheMatriz' que recebe 'lin' (linhas) e 'col' (colunas) como inteiros
    # e retorna uma lista de listas de inteiros (uma matriz).

    m = [[int(randint(0, 5)) for j in range(col)] for i in range(lin)]
    # Cria a matriz 'm' usando uma 'list comprehension' aninhada:
    # - O loop externo 'for i in range(lin)' itera pelas linhas.
    # - O loop interno 'for j in range(col)' itera pelas colunas.
    # - 'randint(0, 5)' gera um número inteiro aleatório entre 0 e 5 (inclusive) para cada elemento.
    # - 'int()' é usado para garantir que o resultado seja um inteiro (embora 'randint' já retorne int).
    
    return m # Retorna a matriz preenchida.

def imprimeMatriz(mat: List[List[int]]) -> None:
    # Define a função 'imprimeMatriz' que recebe uma matriz ('mat' - lista de listas de inteiros)
    # e não retorna nada ('-> None').

    for linha in mat:
        # Itera sobre cada 'linha' dentro da matriz 'mat'.
        print(linha)
        # Imprime a lista que representa a linha atual da matriz.
        
def calcularElemento(a: List[List[int]], b: List[List[int]], i, j) -> int:
    # Define a função 'calcularElemento' que calcula o elemento na posição (i, j)
    # da matriz resultante da multiplicação de A e B.
    
    # Recebe as matrizes 'a' e 'b', e os índices 'i' (linha) e 'j' (coluna).
    
    # Retorna o valor inteiro do elemento calculado.
    
    x = 0
    # Inicializa a variável 'x' (o valor do elemento resultante) com zero.
    
    for z in range(len(a[0])):
        # Itera sobre 'z' (o índice da coluna de A e da linha de B) no intervalo 
        # do número de colunas de A (que deve ser igual ao número de linhas de B,
        # ou seja, len(a[0])).
        
        x += a[i][z] * b[z][j] #fixa a linha do A "[i]" e a coluna do B "[j]"

        # Realiza a multiplicação do elemento A[i][z] pelo elemento B[z][j] e
        # soma o resultado a 'x'. Isso implementa o produto escalar da linha 'i' de A
        # pela coluna 'j' de B.

    return x # Retorna o valor final do elemento calculado.


def multiplicacao(a: List[List[int]], b: List[List[int]]) -> List[List[int]]: 
    # Define a função 'multiplicacao' que recebe duas matrizes 'a' e 'b'
    # e retorna a matriz resultante ('List[List[int]]').

    # A multiplicação só é possível se o número de colunas de A for igual ao número de linhas de B.
    
    m = []
    # Inicializa 'm', a lista de listas que armazenará a matriz resultante.
    
    for i in range(len(a)):
        # Itera sobre as linhas 'i' da matriz A (determina as linhas da matriz resultante).
    
        submat = []
        # Inicializa 'submat', uma lista que armazenará a linha atual da matriz resultante.
        
        for j in range(len(b[0])):
            # Itera sobre as colunas 'j' da matriz B (determina as colunas da matriz resultante).
            
            x = calcularElemento(a, b, i, j)
            # Chama a função auxiliar para calcular o valor do elemento na posição (i, j).
            
            submat.append(x)
            # Adiciona o elemento calculado 'x' à linha atual 'submat'.
        
        m.append(submat)
        # Adiciona a linha completa 'submat' à matriz resultante 'm'.
    
    return m # Retorna a matriz produto.

def main() -> None:
    # Define a função principal 'main', que executa o fluxo do programa.
    # Não retorna nada ('-> None').

    m1 = preencheMatriz(3, 2)
    # Cria a matriz m1 com 3 linhas e 2 colunas.

    m2 = preencheMatriz(2, 3)
    # Cria a matriz m2 com 2 linhas e 3 colunas. A multiplicação m1 x m2 é válida (2 colunas de m1 = 2 linhas de m2).

    imprimeMatriz(m1)
    # Imprime a matriz m1.

    print(f"é")
    # Imprime a string de separação.

    imprimeMatriz(m2)
    # Imprime a matriz m2.

    print(f"o resultado é:")
    # Imprime a string indicando o resultado.

    imprimeMatriz(multiplicacao(m1, m2))
    # Calcula a multiplicação de m1 por m2 e imprime a matriz resultante.
    
if __name__ == "__main__":
    main()
    # Chama a função principal para iniciar a execução do programa.