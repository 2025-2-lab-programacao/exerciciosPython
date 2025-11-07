'''Implemente uma função em Python para comparar as notas de alguns alunos
na primeira prova e na segunda prova aplicada por um professor. A função deve
receber como parâmetro duas listas de tuplas, onde cada tupla contém o nome
de um aluno e sua nota em uma prova. A função deve exibir os seguintes
resultados:

a) Alunos que melhoraram suas notas da primeira prova para a segunda.
b) Alunos que pioraram suas notas.
c) Alunos que mantiveram a mesma nota.
'''

from math import sqrt
# Importa a função 'sqrt' (raiz quadrada) do módulo 'math'.
# Embora importada, esta ferramenta específica ('sqrt') não é utilizada no código subsequente.
from random import randint, random
# Importa as funções 'randint' e 'random' do módulo 'random'.
# 'randint' (inteiro aleatório) não é usada.
# 'random' (número de ponto flutuante aleatório entre 0.0 e 1.0) é usada para gerar notas.
from typing import List
# Importa o tipo 'List' do módulo 'typing', usado para anotação de tipos, indicando que uma variável ou retorno é uma lista.

#gerar lista de pontos
# a: list[tuple]

def gerarTuple() -> tuple:
    # Define a função 'gerarTuple' que cria uma tupla contendo (nome do aluno, nota).
    # Retorna uma tupla.
    nome = input(f"Digite o nome")
    # Solicita ao usuário que digite o nome do aluno. 'input()' lê a entrada como string.
    nota = round((random()*10), 2)
    # Gera a nota: 'random()' gera um float entre 0.0 e 1.0. Multiplica por 10 para ter notas de 0 a 10.
    # 'round(..., 2)' arredonda o resultado para duas casas decimais.
    tupla = (nome, nota)
    # Cria uma tupla com o nome e a nota.
    return tupla
    # Retorna a tupla gerada.

def gerarTupleList(qtd: int) -> List[tuple]:
    # Define a função 'gerarTupleList' que cria uma lista de tuplas.
    # Recebe 'qtd' (quantidade de alunos/tuplas) como inteiro.
    # Retorna uma lista de tuplas.
    tupleList = []
    # Inicializa uma lista vazia chamada 'tupleList' para armazenar as tuplas.
    for i in range(qtd):
        # Inicia um loop 'for' que se repete 'qtd' vezes.
        tupla = gerarTuple()
        # Chama a função 'gerarTuple' para criar uma nova tupla (nome, nota).
        tupleList.append(tupla)
        # O método '.append()' adiciona a tupla gerada ao final da 'tupleList'.
        
    return tupleList
    # Retorna a lista de tuplas preenchida.

def comparaNotas(nota1: dict, nota2: dict):
    # Define a função principal 'comparaNotas' para realizar a análise.
    # Recebe dois dicionários, 'nota1' (notas da primeira prova) e 'nota2' (notas da segunda prova).
    # A estrutura esperada é {nome_do_aluno: nota}.
    melhoria = []
    # Inicializa uma lista vazia para armazenar os nomes dos alunos que melhoraram.
    piora = []
    # Inicializa uma lista vazia para armazenar os nomes dos alunos que pioraram.
    neutro = []
    # Inicializa uma lista vazia para armazenar os nomes dos alunos que mantiveram a mesma nota.
    
    for chave, valor in nota1.items():
        # Itera sobre os pares chave-valor do dicionário 'nota1'.
        # 'chave' é o nome do aluno (string) e 'valor' é a nota da primeira prova (float).
        # O método '.items()' retorna uma visão dos pares (chave, valor) do dicionário.
        valor2 = nota2.get(chave)
        # O método '.get(chave)' busca a nota do aluno na segunda prova ('nota2') usando o nome ('chave').
        # Garante que, se o aluno não estiver em 'nota2', 'valor2' será None (embora o 'main' garanta que estejam).
        if valor > valor2:
            # Compara: Se a nota da primeira prova ('valor') for MAIOR que a da segunda prova ('valor2').
            piora.append(chave)
            # Adiciona o nome do aluno ('chave') à lista de quem piorou. (Instrução b)
        elif valor < valor2:
            # Compara: Se a nota da primeira prova ('valor') for MENOR que a da segunda prova ('valor2').
            melhoria.append(chave)
            # Adiciona o nome do aluno ('chave') à lista de quem melhorou. (Instrução a)
        else:
            # Se nenhuma das condições anteriores for verdadeira (ou seja, valor == valor2).
            neutro.append(chave)
            # Adiciona o nome do aluno ('chave') à lista de quem manteve a nota. (Instrução c)
            
    print(f"Melhoraram: {melhoria}")
    # Imprime a lista de alunos que melhoraram
    
    print(f"Pioraram: {piora}")
    # Imprime a lista de alunos que pioraram.
    
    print(f"Não mudaram: {neutro}")
    # Imprime a lista de alunos que não mudaram a nota.

# funcao main()
def main():
    # Define a função 'main', que executa o fluxo principal do programa.
    listaTupla1 = gerarTupleList(2)
    # Chama 'gerarTupleList' para criar a lista de tuplas da primeira prova para 2 alunos.
    listaTupla2 = gerarTupleList(2)
    # Chama 'gerarTupleList' para criar a lista de tuplas da segunda prova para 2 alunos.
    print(listaTupla1)
    # Imprime a lista de tuplas da primeira prova.
    print(listaTupla2)
    # Imprime a lista de tuplas da segunda prova.
    
    dict1 = dict(listaTupla1)
    # Converte a 'listaTupla1' em um dicionário 'dict1'. 
    # Python converte listas de tuplas (chave, valor) automaticamente.
    dict2 = dict(listaTupla2)
    # Converte a 'listaTupla2' em um dicionário 'dict2'.
    
    comparaNotas(dict1, dict2)
    # Chama a função 'comparaNotas' com os dois dicionários para realizar a análise e imprimir os resultados.
    
    print(dict1)
    # Imprime o dicionário da primeira prova.
    print(dict2)
    # Imprime o dicionário da segunda prova.
    
    
if __name__ == '__main__':
    # Bloco condicional padrão em Python. Garante que a função 'main()' será executada
    # apenas se o script for rodado diretamente (e não importado como um módulo).
    main()
    # Chama a função principal para iniciar a execução do programa.