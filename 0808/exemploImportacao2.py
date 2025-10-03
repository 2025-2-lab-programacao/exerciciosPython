from funcLacoRepDouble import lacoRepDouble;

CasasDec = int(input("Insira a quantidade de casas do tabuleiro: "))
GraoInici = int(input("Insira a quantidade de grãos dispostos inicialmente: "))

graoFinal = lacoRepDouble(CasasDec,GraoInici)
print("O numero de grãos que o monge devera receber é ",graoFinal)