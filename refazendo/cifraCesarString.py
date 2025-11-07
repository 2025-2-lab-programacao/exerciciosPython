
def pularCaracteres(text: str, jump:int):
    res = ""

    for letra in text:
        if letra.isalpha():
            res += chr(ord(letra)+jump)

    return res
    


def main():
    palavra = input(f"Digite uma palavra")
    jump = int(input(f"Digite quantos caracteres a frente"))

    print(f"{pularCaracteres(palavra, jump)}")


if __name__ == "__main__":
    main()