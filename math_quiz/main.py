#1.
x = 0
while (300+x)/20 != x/5:
  x += 1
print("1.:", x)

#9.
x = 198
prim_x = []
y = 308
prim_y = []
lnko = []

oszto_x = 2
while x > 1:
    if x % oszto_x == 0:
        prim_x.append(oszto_x)
        x = x // oszto_x
    else:
        oszto_x = oszto_x + 1

oszto_y = 2
while y > 1:
    if y % oszto_y == 0:
        prim_y.append(oszto_y)
        y = y // oszto_y
    else:
        oszto_y = oszto_y + 1

for i in range(len(prim_x)):
    if prim_x[i] in prim_y:
        lnko.append(prim_x[i])

oszto = 1
for i in range(len(lnko)):
    oszto *= lnko[i]

print(f"9.: {round(198/oszto)}")
