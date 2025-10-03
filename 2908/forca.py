import random

# Função responsável por pedir palavras ao jogador e armazená-las em uma lista
def definirPalavras():
    palavras = []
    for i in range(2):  # Aqui define quantas palavras o jogador deve informar
        # Input de palavra, convertida para minúsculo
        palavras.append(input("Informe uma palavra: ").lower())
    return palavras

# Função principal do jogo
def jogar(lista: list):
    chances = 6
    
    palavra_secreta = random.choice(lista)

    tamanho = len(palavra_secreta)

    letras_acertadas = [False] * tamanho  # Lista de controle para marcar letras já acertadas
    
    
    while chances > 0 and False in letras_acertadas:
        
        # Mostrar a palavra: "_" para letras não acertadas, letra real para as já descobertas
        for i in range(len(palavra_secreta)):
            if letras_acertadas[i] == False:
                print("_", end=" ")
            else:
                print(f"{palavra_secreta[i]}", end=" ")
                
        tentativa = input(f"\nDigite uma letra: ").lower()
        
        # Flag para verificar se a letra existe na palavra
        letra_encontrada = False
        
        for i in range(len(palavra_secreta)):
            if tentativa == palavra_secreta[i]:
                letra_encontrada = True
                letras_acertadas[i] = True  # Marca posição como descoberta
            
            # Se percorreu a palavra inteira e não achou a letra, perde uma chance
            elif (i == len(palavra_secreta) - 1 and letra_encontrada == False):
                chances -= 1
                print(f"Chances restantes: {chances}")
    
    # Condição de derrota
    if chances == 0:
        print(f"\nInfelizmente, você perdeu! A palavra era: {palavra_secreta}")
    
    # Condição de vitória
    else:
        print(f"\n{palavra_secreta}")
        print(f"Parabéns, você ganhou!")


# Função principal que inicia o jogo
def main():
    lista_palavras = definirPalavras() 
    
    print(lista_palavras)
    
    jogar(lista_palavras) 
    
# Ponto de entrada do programa
if __name__ == "__main__":
    main()
