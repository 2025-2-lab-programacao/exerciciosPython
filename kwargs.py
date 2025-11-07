#Empacotamento nomeado (**kwargs): quando você usa **kwargs, ele "reúne" um
#número qualquer de argumentos nomeados em um dicionário

def mostrarInfos(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrarInfos(nome="João", idade=25, cidade="São Paulo")

mostrarInfos(nome="João", idade=25, cidade="São Paulo", estado="São Paulo")

mostrarInfos(nome="João", idade=25, cidade="São Paulo", estado="São Paulo", mãe="Joana")