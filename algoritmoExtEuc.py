"""a = int(input("Ingresa a >"))
b = int(input("Ingresa b >"))
x = [0, 0, 0]
y = [0, 0, 0]
r = [0, 0, 0]
q = [0, 0, 0]
i = 0

r[i] = a
x[i] = 1
y[i] = 0
i += 1

r[i] = b
x[i] = 0
y[i] = 1


flag = True

while(flag == True):
    i += 1
    if(i == 0):
        r[i] = r[i+1] % r[i+2]
        q[i+1] = r[i+1] // r[i+2]
        x[i] = x[i+1] - q[i+1] * x[i+2]
        y[i] = y[i+1] - q[i+1] * y[i+2]
        if(r[i] == 1):
            flag = False
            break
    elif(i == 1):
        r[i] = r[i+1] % r[i-1]
        q[i+1] = r[i+1] // r[i-1]
        x[i] = x[i+1] - q[i+1] * x[i-1]
        y[i] = y[i+1] - q[i+1] * y[i-1]
        if(r[i] == 1):
            break
            flag = False
    elif(i == 2):
        r[i] = r[i-2] % r[i-1]
        q[i-2] = r[i-2] // r[i-1]
        x[i] = x[i-2] - q[i-2] * x[i-1]
        y[i] = y[i-2] - q[i-2] * y[i-1]
        if(r[i] == 1):
            break
            flag = False
    if(i == 2):
        i = -1

print("y = {}".format(y))
print("r = {}".format(r))
"""
a = 1759
b = 550
#     n n-1 n-2
r = [ 1, 0, 0]
q = [ 0, 0, 0]
x = [ 0, 0, 0]
y = [ 0, 0, 0]
n = 1
x[1] = 0
x[2] = 1

y[1] = 1
y[2] = 0

r[1] = a
r[2] = b

while( r[0] != 0 ):
    
    r[0] = r[2] % r[1]
    q[0] = r[2] // r[1]
    x[0] = x[2] - q[0] * x[1]
    y[0] = y[2] - q[0] * y[1]

    print( "{} {} {} {} ".format(r[0], q[0], x[0], y[0]))
    r[2] = r[1]
    r[1] = r[0]

    x[2] = x[1]
    x[1] = x[0]

    y[2] = y[1]
    y[1] = y[0]


print("*******")
print("({})X({}) + ({})X({})".format(a, y[2], b,x[2] ))
"""print(r)
print(x)
print(y)
print(q)

"""
