def verificar_primo(num: int) -> bool:
    v = True
    raiz = int(num ** (1/2))
    for i in range(1, raiz+1):
        if(num%i == 0 and (i!=num and i!=1)):
            v = False
            break
    return v


# funcao para gerar os valores primos
def gerar_primos(cont) -> list:
    lista = []
    i = 2
    while len(lista) < cont:
        if(verificar_primo(i)):
            lista.append(i)
        i+=1

    return lista

def imprimir_lista(lt: list) -> None:
    print(lt)
    

# funcao principal --> main
def main() -> None:
    a = int(input(f"Digite a qtd de números desejada: "))
    vetor = gerar_primos(a)
    imprimir_lista(vetor)    
    
main()

# programa principal