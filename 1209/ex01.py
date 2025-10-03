from random import randint

a = []
b = []

for i in range(5): 
    a.append(int(input()))

for i in range(5):
        aux = randint(1, 10)
        
        if aux not in a:
            a.append(int(input()))        
            
print(a)