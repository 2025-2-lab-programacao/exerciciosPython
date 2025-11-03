from random import random

def consultar():
    with open('clientes.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            nome, pv = linha.split(';')
            
            pv = float(pv)
            
            juros = round(random()/2, 2)
            prazo = 12
            
            pmt = pv * (juros * ((juros+1) ** prazo)) / ((juros+1)**prazo - 1)
            
            print(f"{nome} -> valor financiado: {pv} | valor de financiamento: {pmt:.2f}")
             

# funcao main()
def main():
    consultar()
    
    
if __name__ == '__main__':
    main()