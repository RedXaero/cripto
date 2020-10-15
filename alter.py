M = int(input("Ingresa M >"))
e = int(input("Ingresa e >"))
n = int(input("Ingresa n >"))

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