# funcao mdf
def mdc(m: int, n: int) -> int:
    if n > m:
        return mdc(n, m)
    elif n == 0:
        return m
    return mdc(n, m%n)
    
#função principal
def main():
    m = int(input("Informe o primeiro valor: "))
    n = int(input("Informe o segundo valor: "))
    print(f"mdc({m}, {n}) = {mdc(m,n)}")
            
# programa principal
if __name__ == '__main__':
    main()
