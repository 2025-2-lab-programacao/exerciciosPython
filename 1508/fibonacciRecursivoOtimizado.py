# programa com funcao recursiva para ler um valor inteiro e 
# positivo e retorne o valor de fibonancci

def fibonacci(num: int, vec: list) -> int:
    if(num == 1 or num == 2):
        return vec[num-1]
    else:
        if vec[num-1] == 0:
            vec[num-1] = (fibonacci(num-1, vec) + fibonacci(num-2, vec))

        return vec[num-1]

def main() -> None:
    a = int(input(f"Digite o valor: "))
    b = [0] * a
    b[0], b[1] = 1,1
    print(fibonacci(a, b))
    
        
if __name__ == "__main__":
    main()