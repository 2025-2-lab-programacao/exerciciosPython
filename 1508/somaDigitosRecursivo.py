''''
Escreva um programa em python que tenha um método recursivo
que calcule a soma dos dígitos de um número inteiro informado via teclado.
'''

def somaDig(num, len: int) -> int:
    if(len == 0):
        return int(num[len])
    else:
        return int(num[len]) + somaDig(num, len-1)

def main() -> None:
    a = input(f"Digite um número inteiro: ")
    print(somaDig(a, len(a)-1))
    

    
if __name__ == "__main__":
    main()