# a partir de uma lista de palavras (que pode haver 
# repetição), imprimir a quantidade de vezes que cada
# palavra aparece. Por último, imprimir a ocorrencia de cada letra.

# entrada
lista = []
# Inicializa uma lista vazia chamada 'lista', que armazenará as palavras fornecidas pelo usuário.

total = int(input("Qual o total de palavras?"))
# Solicita ao usuário o número total de palavras que serão inseridas.

for i in range(total):

    lista.append(input("Palavra: "))
    # Solicita uma palavra ao usuário em cada iteração usando 'input("Palavra: ")'.
    # O método '.append()' da lista adiciona a palavra digitada ao final da lista 'lista'.
    
# contar o numero de ocorrencia de cada uma das palavras
ocorrencia = {}
# Inicializa um dicionário vazio chamado 'ocorrencia'.
# Dicionários em Python (pares chave: valor) são ideais para contagem, onde a chave será a palavra e o valor será sua contagem.

for palavra in lista:
    # Inicia um loop 'for' para iterar sobre cada 'palavra' na lista de palavras inseridas.

    if palavra in ocorrencia:
        # Verifica se a 'palavra' atual já existe como chave no dicionário 'ocorrencia'.
        ocorrencia[palavra] += 1
        # Se a palavra já existe, incrementa o valor (contagem) associado a essa chave em 1.
    else:
        # Se a palavra ainda não foi encontrada e não está no dicionário.
        ocorrencia[palavra] = 1
        # Adiciona a 'palavra' como uma nova chave ao dicionário e define seu valor inicial (contagem) como 1.
        
print(ocorrencia)
# Imprime o dicionário completo 'ocorrencia'. A saída será no formato {palavra1: contagem1, palavra2: contagem2, ...}.

for chave, valor in ocorrencia.items():
    # Inicia um loop 'for' para iterar sobre os pares chave-valor do dicionário 'ocorrencia'.
    # O método '.items()' retorna uma visão dos pares (chave, valor) do dicionário.
    # 'chave' representa a palavra e 'valor' representa a contagem.

    print(f'{chave} --> {valor}')
    # Imprime a palavra ('chave') e sua contagem ('valor') de forma formatada.
   
    

# OBS: Embora inicializada, esta lista não é utilizada no código subsequente.

letras = {}
# Inicializa um dicionário vazio chamado 'letras' para armazenar a contagem de ocorrências de cada letra.

for palavra in lista:
    # Inicia o loop externo, iterando sobre cada 'palavra' na lista de entrada.
    
    for letra in palavra:
        # Inicia o loop interno, iterando sobre cada 'letra' dentro da 'palavra' atual.
        # Strings em Python podem ser iteradas como sequências de caracteres.
    
        if letra in letras:
            # Verifica se a 'letra' atual já existe como chave no dicionário 'letras'.
            
            letras[letra] += 1
            # Se a letra já existe, incrementa sua contagem em 1.
        else:
            # Se a letra ainda não foi encontrada.
            letras[letra] = 1
            # Adiciona a 'letra' como uma nova chave ao dicionário e define sua contagem inicial como 1.
print(letras)
# Imprime o dicionário final 'letras', mostrando a contagem total de cada letra em todas as palavras da lista.