from random import randint

len = int(input("digite ai: "))

a = []
aux = []

for i in range(len):
    aux = []
    for j in range(len):
        aux.append(randint(1,50))
    a.append(aux)
    
print(a)

somaDp = 0
somaDs = 0

for i in range(len):
    for j in range(len):
        if i == j:
            somaDp += a[i][j]
        if (i+j) == len-1:
            somaDs += a[i][j]
            
print(f"A soma da diagonal principal é {somaDp} e da secundária é {somaDs}")


for i in range(len//2):
    for j in range(len//2):
            somaDp += a[i][i]
            somaDs += a[i][len-1-i]
            
print(f"A soma da diagonal principal é {somaDp} e da secundária é {somaDs}")