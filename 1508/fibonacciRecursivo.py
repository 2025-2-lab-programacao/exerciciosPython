# programa com funcao recursiva para ler um valor inteiro e 
# positivo e retorne o valor de fibonancci
def fibonacci(num: int) -> int:
    if(num == 1 or num == 2):
        return 1
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

def main() -> None:
    a = int(input(f"Digite o valor: "))
    print(fibonacci(a))
        
if __name__ == "__main__":
    main()