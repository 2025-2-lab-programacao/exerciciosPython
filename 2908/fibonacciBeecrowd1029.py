chamada = 0

def fib(x):
    global chamada
    chamada += 1  # conta cada chamada
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)

# programa principal
n = int(input())
for i in range(n):
    x = int(input())
    chamada = 0
    f = fib(x)
    print(f"fib({x}) = {chamada - 1} calls = {f}")
