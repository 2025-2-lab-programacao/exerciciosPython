row = int(input())
column = int(input())

m = []
for i in range(row):
    aux = []
    for j in range(column):
        aux.append(int(input()))
    m.append(aux)

print(m)