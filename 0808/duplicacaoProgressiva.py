def lacoRepDouble(a,b):
    c=0
    for i in range (a+1):
        c += b
        b = b*2
    return c