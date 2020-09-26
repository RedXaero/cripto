# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:02:26 2020

@author: Mariela Leticia Martínez Hernández
"""

#from IPython import get_ipython
#get_ipython().magic('reset -sf')

import random

def main():
    
    op_menuP=1
    while op_menuP<6:
        print("\n ********** ALGORITMO RSA ********** ")

        print("\n¿Qué operación desea realizar?\n")
        print("     1. Cálculo M.C.D - Algoritmo de Euclides.")
        print("     2. Cálculo de inverso multiplicativo - Algoritmo extendido de Euclides.")
        print("     3. Generación de par de llaves RSA.")
        print("     4. Cifrado RSA.")
        print("     5. Descifrado RSA.")
        print("     6. Salir")
        
        opcion=int(input("\nIndique el número de opción: "))
        
        if opcion==1:
            mcd=MaxComunDivisor()
            print ("\n     m.c.d. : ",mcd)
            
        elif opcion==2:
            InvMultiplicativo()
            
        elif opcion==3:
            GenKeys()
            
        elif opcion==4:
            CifradoRSA()
            
        elif opcion==5:
            DescifradoRSA()
            
        else:
            print("Saliendo del programa...")
            op_menuP=6

def MaxComunDivisor():
    print("\n++++++++++ Cálculo de Máximo Común Divisor ++++++++++")
    a=int(input("     Ingrese entero a: "))
    b=int(input("     Ingrese entero b: "))
    mcd=Euclides(a,b)
    return mcd

def InvMultiplicativo():
    print("\n++++++++++ Algoritmo Extendido de Euclides ++++++++++")
    a=int(input("     Ingrese entero a: "))
    b=int(input("     Ingrese entero b: "))
    gcd,x,y = gcdExtended(a,b)
    print("\n     m.c.d: ",gcd)
    print("\n     x: ",x)
    print("\n     y: ",y)

def gcdExtended(a, b):  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)  
      
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y

def GenKeys():
    print("\n++++++++++ Generación de llaves RSA ++++++++++")
    
    print("\n--> Selección de 2 primos aleatorios entre 2 y 10,000")
    p=EligePrimo()
    q=EligePrimo()
    while p==q:
        q=EligePrimo()
    print("     Primo 1: ",p)
    print("     Primo 2: ",q)
    
    pq=p*q
    print("\n --> Calcular n = p * q")
    print("     n: ",pq)
    
    print("\n --> Calcular función Euler's Totient, de n")
    print("     p-1: ",(p-1))
    print("     q-1: ",(q-1))
    tot=(p-1)*(q-1)
    print("     Función Euler's Totient de n: ",tot)
    
    e=SeleccionaE(tot)
    print("\n--> Seleccionamos e")
    print("     e: ", e)
    
    print("\n--> Determinamos d")
    
    gcd,d,y = gcdExtended(e,tot)
    if d<0:
        d=d%tot
    print("     d: ",d)
    
    print("\nLlave pública={",e,",",pq,"}")
    print("\nLlave privada={",d,",",pq,"}")

def CifradoRSA():
    plaintext=[]
    ciphertext=[]
    print("\n++++++++++ CIFRADO RSA ++++++++++")
    mensaje=input("\n     Ingrese mensaje a cifrar (Texto ASCII): ")
    
    for i in mensaje:
        plaintext.append(ord(i))
    
    #print("Valores decimal del mensaje: ",plaintext)
    
    print("--> Ingrese elementos de la Llave para Cifrar: ")
    e=int(input("     Ingrese valor de e: "))
    n=int(input("     Ingrese valor de n: "))
    
    for m in plaintext:
        c=pow(m,e,n)
        ciphertext.append(c)
    
    print("\n     Mensaje cifrado: \n")
    for n in ciphertext:
        print(n,end=":")
    
    print("\n\n\n")
    
def DescifradoRSA():
    ciphertext=[]
    plaintext=[]
    textoclaro=[]
    
    print("\n++++++++++ DESCIFRADO RSA ++++++++++")
    print("\n     Ingrese mensaje a descifrar. Por ejemplo:")
    print("\n     26509202:24353726:48920114:18885770:24447983:6649180:42304389:18885770:")
    ciphertext=input("\n     Ciphertext: ")
    
    print("\n")
    ciphertext=(ciphertext.split(':'))
    
    ind=len(ciphertext)
    if ciphertext[ind-1]=='':
        del ciphertext[ind-1]
    
    for i in range(0, len(ciphertext)): 
        ciphertext[i] = int(ciphertext[i])
    
    #print(ciphertext)
    
    print("--> Ingrese elementos de la Llave para Descifrar: ")
    d=int(input("     Ingrese valor de d: "))
    n=int(input("     Ingrese valor de n: "))
    
    for c in ciphertext:
        m=pow(c,d,n)
        plaintext.append(m)
    
    print("\n     Mensaje descifrado: \n")
    for p in plaintext:
        char=chr(p)
        textoclaro.append(char)
        
    for t in textoclaro:
        print(t,end="")
    
    print("\n\n\n")


def power(x, y, p): 
    res = 1;  
    x = x % p;  
    while (y > 0): 
        if (y & 1): 
            res = (res * x) % p; 
        y = y>>1;
        x = (x * x) % p; 
    return res; 

def MillerTest(d, n): 

    a = 2 + random.randint(1, n - 4); 
    x = power(a, d, n); 
  
    if (x == 1 or x == n - 1): 
        return True; 

    while (d != n - 1): 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1): 
            return False; 
        if (x == n - 1): 
            return True; 

    return False; 

def isPrime( n, k): 

    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 

    d = n - 1; 
    while (d % 2 == 0): 
        d //= 2; 

    for i in range(k): 
        if (MillerTest(d, n) == False): 
            return False; 
  
    return True;

def EligePrimo():
    Primos=[]
    
    k=4
    for n in range(1,10000):
        if(isPrime(n, k)):
            Primos.append(n)
    return random.choice(Primos)

def Euclides(a,b):
    if b==0:
        return a
    else:
        return Euclides(b,a%b)

def SeleccionaE(tot):
    cont=0
    PosiblesE=[]
    
    while cont<30:
        for i in range(3,tot):
            residuo=Euclides(i,tot)
            if residuo==1:
                #print("Primo relativo encontrado:",i)
                PosiblesE.append(i)
                cont = cont + 1
                if cont==30:
                    break
        break
    return random.choice(PosiblesE)

if __name__ == '__main__':
    main()