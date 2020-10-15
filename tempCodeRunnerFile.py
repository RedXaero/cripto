cont = 1
aux = 1
while((e//2) != 0):
    if((e%2) != 0):
        aux *= pow(M, cont, n)
    cont *= 2
    e //= 2
aux *= pow(M, cont, n)
aux %= n
print(aux)