
a = 1741
b = 551
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
    # print("r = {},  q = {}, x = {}, y = {}".format(r[0], q[0], x[0], y[0]))
  
    r[2] = r[1]
    r[1] = r[0]

    x[2] = x[1]
    x[1] = x[0]

    y[2] = y[1]
    y[1] = y[0]


print("*******")
print("({})X({}) + ({})X({})".format(a, y[2], b,x[2] ))
if(y[1] >= 1):
    print("d = {}".format(x[2]))
else:
    print("El inverso no existe");
"""
print(r)
print(x)
print(y)
print(q)"""