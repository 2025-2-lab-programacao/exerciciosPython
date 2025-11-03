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
from random import randint, random
from typing import List

#gerar lista de pontos
# a: list[tuple]

def gerarTuple() -> tuple:
    nome = input(f"Digite o nome")
    nota = round((random()*10), 2)
    tupla = (nome, nota)
    return tupla

def gerarTupleList(qtd: int) -> List[tuple]:
    tupleList = []
    for i in range(qtd):
        tupla = gerarTuple()
        tupleList.append(tupla)
        
    return tupleList

def comparaNotas(nota1: dict, nota2: dict):
    melhoria = []
    piora = []
    neutro = []
    
    for chave, valor in nota1.items():
        valor2 = nota2.get(chave)
        if valor > valor2:
            piora.append(chave)
        elif valor < valor2:
            melhoria.append(chave)
        else:
            neutro.append(chave)
        
    print(f"Melhoraram: {melhoria}")
    
    print(f"Pioraram: {piora}")
    
    print(f"Não mudaram: {neutro}")

# funcao main()
def main():
    listaTupla1 = gerarTupleList(2)
    listaTupla2 = gerarTupleList(2)
    print(listaTupla1)
    print(listaTupla2)
    
    dict1 = dict(listaTupla1)
    dict2 = dict(listaTupla2)
    
    comparaNotas(dict1, dict2)
    
    print(dict1)
    print(dict2)
    
    
if __name__ == '__main__':
    main()