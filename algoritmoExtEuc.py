a = int(input("Ingresa a >"))
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
