#Empacotamento nomeado (**kwargs): quando você usa **kwargs, ele "reúne" um
#número qualquer de argumentos nomeados em um dicionário

def mostrarInfos(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrarInfos(nome="João", idade=25, cidade="São Paulo")

mostrarInfos(nome="João", idade=25, cidade="São Paulo", estado="São Paulo")

mostrarInfos(nome="João", idade=25, cidade="São Paulo", estado="São Paulo", mãe="Joana")

#o kwargs é basicamente para quando você não sabe quantos argumentos nomeados (ou seja, com nome e valor) serão passados

#O zip junta duas tuplas em um dicionário

tupla1 = (10, 20, 30)
tupla2 = ('x', 'y', 'z')
combinado = zip(tupla1, tupla2)
print(list(combinado))
# Saída: [(10, 'x'), (20, 'y'), (30, 'z')]

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
for num, letra in zip(numeros, letras):
    print(f"Número: {num}, Letra: {letra}")
    
# Saída:
# Número: 1, Letra: a
# Número: 2, Letra: b
# Número: 3, Letra: c