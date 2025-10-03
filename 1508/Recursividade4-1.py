''''Escreva um programa em python que contenha um método recursivo que calcule o valor de 
x^n. O valor de n deve ser maior ou igual a 0'''

def exp(a: int, b: int) -> int:
    if(b == 0):
        return 1
    else:
        return a * exp(a, b-1)

def main() -> None:
    x = int(input(f"Digite o valor da base"))
    n = int(input(f"Digite o valor do expoente (maior ou igual a 0)"))
    
    print(exp(x,n))
    
if __name__ == "__main__":
    main()