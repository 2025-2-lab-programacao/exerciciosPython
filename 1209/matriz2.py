row = int(input())
column  = int(input())

# m = [[] for  i in range(linha)]

m = [[int(input()) for j in range(column)] for i in range(row)]

print(m)