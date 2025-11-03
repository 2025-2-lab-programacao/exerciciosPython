t = tuple('python')
print(t)
print(t[0])
print(t[1:3])

# gera erro porque uma tupla é imutável
#t[0] = 'j'

# Como tuplas são imutáveis, os elementos não 
# podem ser alterados, mas podem ser substituídos

t = tuple('python')
t = ('A',) + t[1:]
print(t)

# atribuição de tupla

#t = 1, 2, 3
t = (1, 2, 3)
print(t) # Saída: (1, 2, 3)