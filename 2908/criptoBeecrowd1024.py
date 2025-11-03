
def etapa1(texto: str) -> str:
    res = ""
    for i in texto:
        if i.isalpha():
            res += chr(ord(i) + 3)
        else:
            res += i
               
    return res

def etapa2(texto: str) -> str:
    invertida = texto[::-1]
    return invertida

def etapa3(texto: str) -> str:
    met = int((len(texto)) // 2)
    
    result = ""
    for i in range(len(texto)):
        if i < met:
            result += texto[i]
        else:
            result += chr(ord(texto[i])-1)
            
    return result
    
    

def main():
    qtd = int(input())
    
    for i in range(qtd):
        frase = input()
        novoTexto = etapa1(frase)
        novoTexto = etapa2(novoTexto)
        novoTexto = etapa3(novoTexto)
        print(novoTexto, end="\n")

if __name__ == "__main__":
    main()