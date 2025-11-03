def fat(num: int) -> int : 
    if num == 0: return 1
    else:
        return (num * fat(num-1))
        
def main() -> None:
    a = int(input("Digite um número inteiro e positivo: "))
    if a<0:
        print(f"O valor deve ser inteiro e positivo")
    else:
        print(fat(a))

if __name__ == "__main__":
    main()