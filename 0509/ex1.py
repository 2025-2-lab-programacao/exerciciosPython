import random

def definirPalavras():
    palavras = []
    for i in range(2):
        palavras.append(input("Informe uma palavra: ").lower())
    return palavras

def jogar(lista: list):
    chances = 6
    segredo = random.choice(lista)
    tamanho = len(segredo)
    right = [False] * tamanho
    
    while chances >0  and False in right:
        for i in range(len(segredo)):
            if right[i] == False:
                print("_", end=" ")
            else: print(f"{segredo[i]}", end=" ")
            
        letra = input(f"\nDigite uma letra: ").lower()
        
        check = False
        for i in range(len(segredo)):
            if letra == segredo[i]:
                check = True
                right[i] = True
            elif(i == len(segredo)-1 and check == False):
                chances -= 1
                print(f"Chances: {chances}")
    
    if chances == 0:
        print(f"Infelizmente, você perdeu!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print(segredo)
        print(f"Parabéns, você ganhou!")
                

def main():
    lista = definirPalavras()
        
    print(lista)
    jogar(lista)
    
if __name__ == "__main__":
    main()