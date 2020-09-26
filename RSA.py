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
print(n)
phi = (p - 1) * (q - 1)

"""e = randint(1, phi - 1)
ale = mcd(phi - 1, e)

while(ale != 1):
    e = randint(1, phi - 1)
    ale = mcd(phi - 1, e)

#print("e = ",e)
"""
e = 7


#AEU
r = [ 1, 0, 0]
q = [ 0, 0, 0]
x = [ 0, 0, 0]
y = [ 0, 0, 0]

x[1] = 0
x[2] = 1

y[1] = 1
y[2] = 0

r[1] = phi
r[2] = e

while( r[0] != 0 ):
    r[0] = r[2] % r[1]
    q[0] = r[2] // r[1]
    x[0] = x[2] - q[0] * x[1]
    y[0] = y[2] - q[0] * y[1]

    r[2] = r[1]
    r[1] = r[0]

    x[2] = x[1]
    x[1] = x[0]

    y[2] = y[1]
    y[1] = y[0]


d = x[2]
print(d)
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