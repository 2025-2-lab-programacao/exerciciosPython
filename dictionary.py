# a partir de uma lista de palavras (que pode haver 
# repetição), imprimir a quantidade de vezes que cada
# palavra aparece. Por último, imprimir a ocorrencia de cada letra.

# entrada
lista = []
total = int(input("Qual o total de palavras?"))
for i in range(total):
    lista.append(input("Palavra: "))
    
# contar o numero de ocorrencia de cada uma das palavras
ocorrencia = {}
for palavra in lista:
    if palavra in ocorrencia:
        ocorrencia[palavra] += 1
    else:
        ocorrencia[palavra] = 1
        
print(ocorrencia) #easiest

for chave, valor in ocorrencia.items():
    print(f'{chave} --> {valor}')
    
listaLetras = []
letras = {}
for palavra in lista:
    for letra in palavra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
print(letras)
