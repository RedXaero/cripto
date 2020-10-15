from random import randint



def mcd(n1,n2):
    res = 0
    while n2 > 0:
        res = n2
        n2 = n1 % n2
        n1 = res
    return n1

M = int(input("Número a encriptar >"))
p = int(input("p >"))
q = int(input("q >"))

n = p * q
print("n = {}".format(n))
phi = (p - 1) * (q - 1)
print("phi = {}".format(phi))




e1 = randint(2, phi - 1)
ale = mcd(phi , e1)
e2 = e1

while(ale != 1):
    e1 += 1
    ale = mcd(phi , e1)
    if(e1 == phi):
        break

if(e1 == phi):
    ale = mcd(phi , e2)
    while(ale != 1):
        e2 -= 1
        ale = mcd(phi , e2)
        if(e2 == 1):
            break
        e1 = e2


print("e = ",e1)

#AEU
d = 1
de = d * e1
res = (de % phi)

while( res != 1):
    d += 1
    de = d * e1
    res = (de % phi)

print( "d = ", d)

print("PU= {}, {} ".format(e1, n))
print("PR= {}, {} ".format(d, n))
#---------------------------------------------
e = e1
cont = 1
aux = 1
while((e//2) != 0):
    if((e%2) != 0):
        aux *= pow(M, cont, n)
    cont *= 2
    e //= 2
aux *= pow(M, cont, n)
aux %= n
print("Encriptado")
print(aux)
C = aux
#---------------------------------------------
cont = 1
aux = 1
e = d
while((e//2) != 0):
    if((e%2) != 0):
        aux *= pow(C, cont, n)
    cont *= 2
    e //= 2
aux *= pow(C, cont, n)

aux %= n
print("Desencriptado")
print(aux)