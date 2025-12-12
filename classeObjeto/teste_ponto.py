from ponto import Ponto

lista = []
quantidade = int(input('Qual a quantidade de pontos? '))
for _ in range(quantidade):
    x = int(input('Digite o valor do eixo x:'))
    y = int(input('Digite o valor do eixo y:'))
    lista.append(Ponto(x, y))
        
# impressão de cada ponto e sua respectiva distância até o centro
print('Distância de cada ponto até a origem (0,0): ')
for p in lista:
    print(f'{p} --> {p.calcular_distancia_ate_origem()}')
    
print()
print(f'Distância entre os pontos 1 e 2')
print(lista[0].calcular_distancia(lista[1]))