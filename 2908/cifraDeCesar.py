def cripto(texto: str, gap: int) -> str:
    resultado = ""
    for i in texto:
        if i.isalpha():
            if 'a' <= i <= 'z':
                novo = chr((ord(i) - ord('a') + gap) % 26 + ord('a'))
                resultado += novo
            elif 'A' <= i <= 'Z':
                novo = chr((ord(i) - ord('A') + gap) % 26 + ord('A'))
                resultado += novo
        else:
            resultado += i
    return resultado


def descripto(texto: str, gap: int) -> str:
    resultado = ""
    for i in texto:
        if i.isalpha():
            if 'a' <= i <= 'z':
                novo = chr((ord(i) - ord('a') - gap) % 26 + ord('a'))
                resultado += novo
            elif 'A' <= i <= 'Z':
                novo = chr((ord(i) - ord('A') - gap) % 26 + ord('A'))
                resultado += novo
        else:
            resultado += i
    return resultado


def main():
    frase = input("Frase: ")
    gap = int(input("Deslocamento (gap): "))

    criptografada = cripto(frase, gap)
    print(f"Criptografada: {criptografada}")

    descriptografada = descripto(criptografada, gap)
    print(f"Descriptografada: {descriptografada}")


if __name__ == "__main__":
    main()
