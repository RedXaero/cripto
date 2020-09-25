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
phi = (p - 1) * (q - 1)

"""e = randint(1, phi - 1)
ale = mcd(phi - 1, e)

while(ale != 1):
    e = randint(1, phi - 1)
    ale = mcd(phi - 1, e)

#print("e = ",e)
"""
e = 5
d = 1
de = d * e
res = (de % phi)

while( res != 1):
    d += 1
    de = d * e
    res = (de % phi)

#print( "d = ", d)

print("PU= {}, {} ".format(e, n))
print("PR= {}, {} ".format(d, n))

C = (M ** e) % n
print("Encriptación >{}".format(C))

M = (C ** d) % n
print("Desencriptación >{}".format(M))