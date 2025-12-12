
notas = [{"nome": "Ihago", 'nota': 10},
         {"nome": "Ricardo", 'nota': 9.9},
         {"nome": "Ihan", 'nota': 10},
         {"nome": "Veiga", 'nota': 7},
         {"nome": "Knorre", 'nota': 8}]

# função para ordenar uma lista pelo método quicksort (pivô como último elemento)
def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)

def particionar(lista, inicio, fim) -> int:  # retorna o índice do pivô
    pivo = lista[fim]['nota']
    i = inicio
    
    for j in range(inicio, fim):
        if lista[j]['nota'] <= pivo:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1

    # coloca o pivô no local correto
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

print(notas)
quicksort(notas)
print(notas)