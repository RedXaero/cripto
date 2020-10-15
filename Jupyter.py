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

"""
    Encriptado
"""
#Encriptado
from random import randint

def mcd(n1,n2):
    res = 0
    while n2 > 0:
        res = n2
        n2 = n1 % n2
        n1 = res
    return n1

M = int(input("Número a encriptar >"))
p = 9973
q = 9967
n = p * q
print("n = {}".format(n))

phi = 99380952
e1 =  69389687
d =  68117063


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


"""
Desencriptado
"""
#Desencriptado
from random import randint

def mcd(n1,n2):
    res = 0
    while n2 > 0:
        res = n2
        n2 = n1 % n2
        n1 = res
    return n1

M = int(input("Número a desencriptar >"))
p = 9973
q = 9967

n = p * q
phi = 99380952
e =  69389687
d =  68117063

#AEU
d = 1
de = d * e1
res = (de % phi)

while( res != 1):
    d += 1
    de = d * e1
    res = (de % phi)

print( "d = ", d)

print("PR= {}, {} ".format(d, n))

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

"""
convirtiendo cadena a ASCII
"""
cad = input("Ingresa el texto a cifrar > ")
asciiEntero = []
cifrada = ""

#conversión de la cadena a su representación ASCII
for i in range(0, len(cad)):
    asciiEntero.append(ord(cad[i]))

#Sugerimos nuestras cadenas de 4 dígitos
#Entonces si la cadena es menor a 3 dígitos se le agrega un 0 al inicio
for i in asciiEntero:
    cifrada += str(i)

#Marcamos el inicio y el fin de las subcadenas, las subcadenas serán de 4 dígitos
ini = 0
fin = 4
cadenas = []

#Recorrido del arreglo obteniendo subcadenas de 4 en 4
for i in range(0, len(cifrada)):
    if fin > len(cifrada):
        fin = len(cifrada)
        
    cadenas.append(str(cifrada[ini:fin]))
    if(fin == len(cifrada)):
        
        break
    ini += 4
    fin += 4

print(cadenas)
textAsc = []

for i in range(0, len(cadenas)):
    textAsc.append(int(cadenas[i]))
    
print(textAsc)


#--- Encriptado

#Encriptado
from random import randint

def mcd(n1,n2):
    res = 0
    while n2 > 0:
        res = n2
        n2 = n1 % n2
        n1 = res
    return n1

cadCif = []
for i in textAsc:    
    M = i
    p = 9973
    q = 9967
    n = p * q
    #print("n = {}".format(n))

    phi = 99380952
    e1 =  69389687
    d =  68117063


    #AEU
    #d = 1
    de = d * e1
    res = (de % phi)

    #while( res != 1):
    #    d += 1
    #    de = d * e1
    #    res = (de % phi)

    #print( "d = ", d)

    #print("PU= {}, {} ".format(e1, n))

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
    cadCif.append(aux)
    
print(cadCif)


"""
Desencriptando cadena
"""
#Desencriptado
from random import randint
cadDes = []
def mcd(n1,n2):
    res = 0
    while n2 > 0:
        res = n2
        n2 = n1 % n2
        n1 = res
    return n1

for i in cadCif:
    C = i
    p = 9973
    q = 9967

    n = p * q
    phi = 99380952
    e =  69389687
    d =  68117063

    #AEU
    #d = 1
    de = d * e1
    res = (de % phi)

    #while( res != 1):
     #   d += 1
      #  de = d * e1
       # res = (de % phi)

    #print( "d = ", d)

    #print("PR= {}, {} ".format(d, n))

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
    cadDes.append(aux)
print(cadDes)


