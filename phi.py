from random import randint

phi = 30

aPhi = []
for i in range(1, phi + 1):
    aPhi.append(randint(2, phi - 1))

for i in range(1, len(aPhi) - 1):
    print(aPhi[i])

