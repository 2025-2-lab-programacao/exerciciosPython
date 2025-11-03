#input n
#print nonlocal
#if n = 1 then Stop
#if n é impar then n <- 3n + 1
#else n <- n/2
#goto 2

def processa(a):
    if(a%2!=0):
        a = (3*a) + 1
    else:
        a = a/2
    return a


n = int(input(f"Digite o número: "))

while(n > 1):
    print(f"{n}")
    n = processa(n)
    

    
    