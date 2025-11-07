"""
Implemente uma função em Python para comparar as notas de alguns alunos
na primeira prova e na segunda prova aplicada por um professor.

A função deve receber como parâmetro duas listas de tuplas, 
onde cada tupla contém o nome de um aluno e sua nota em uma prova. 
A função deve exibir os seguintes resultados:

a) Alunos que melhoraram suas notas da primeira prova para a segunda.
b) Alunos que pioraram suas notas.
c) Alunos que mantiveram a mesma nota.
"""

from random import random
from typing import List, Tuple


def gerar_tupla() -> Tuple[str, float]:
    nome = input("Digite o nome do aluno: ")
    nota = round(random() * 10, 2)
    return nome, nota


def gerar_lista_tuplas(qtd: int) -> List[Tuple[str, float]]:
    return [gerar_tupla() for _ in range(qtd)]


def comparar_notas(prova1: dict, prova2: dict) -> None:
    melhoraram = []
    pioraram = []
    iguais = []

    for aluno, nota1 in prova1.items():
        nota2 = prova2.get(aluno)
        if nota2 is None:
            continue

        if nota2 > nota1:
            melhoraram.append(aluno)
        elif nota2 < nota1:
            pioraram.append(aluno)
        else:
            iguais.append(aluno)

    print(f"\nAlunos que melhoraram: {melhoraram or 'Nenhum'}")
    print(f"Alunos que pioraram: {pioraram or 'Nenhum'}")
    print(f"Alunos que mantiveram a nota: {iguais or 'Nenhum'}")


def main() -> None:
    qtd = int(input("Quantos alunos deseja cadastrar? "))

    print("\n--- Primeira prova ---")
    prova1 = dict(gerar_lista_tuplas(qtd))

    print("\n--- Segunda prova ---")
    prova2 = dict(gerar_lista_tuplas(qtd))

    print("\nNotas da primeira prova:", prova1)
    print("Notas da segunda prova:", prova2)

    comparar_notas(prova1, prova2)


if __name__ == "__main__":
    main()
