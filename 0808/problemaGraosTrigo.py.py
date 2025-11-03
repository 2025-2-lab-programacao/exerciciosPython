'''Uma rainha requisitou os serviços de um monge e disse-lhe que pagaria qualquer
preço. O monge, necessitando de alimentos, perguntou à rainha se o pagamento
poderia ser feito com grãos de trigo dispostos em um tabuleiro de xadrez, de tal
forma que o primeiro quadro contivesse apenas um grão e os quadros
subsequentes, o dobro do quadro anterior. A rainha considerou o pagamento
barato e pediu que o serviço fosse executado, sem se dar conta de que seria
impossível efetuar o pagamento. Escreva um programa em Python para calcular o
número de grãos de trigo que o monge deverá receber. O programa deverá ter
uma função para calcular e retornar o número de grãos de trigo. O cálculo deve
ser realizado por meio de um laço de repetição for.'''

def total():
    c,b = 0,1
    for i in range(0,64):
        b = b*2
        c+= b
    return c

totalgrao = total()
print(totalgrao)