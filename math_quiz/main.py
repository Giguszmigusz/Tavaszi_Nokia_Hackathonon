#1.
x = 0
while (300+x)/20 != x/5:
  x += 1
print("1.:", x)

#9.
a = 198
prim_a = []
m = 308
prim_m = []
lnko = []

oszto_a = 2
while a > 1:
    if a % oszto_a == 0:
        prim_a.append(oszto_a)
        a = a // oszto_a
    else:
        oszto_a = oszto_a + 1

oszto_m = 2
while m > 1:
    if m % oszto_m == 0:
        prim_m.append(oszto_m)
        m = m // oszto_m
    else:
        oszto_m = oszto_m + 1

for i in range(len(prim_a)):
    if prim_a[i] in prim_m:
        lnko.append(prim_a[i])

oszto = 1
for i in range(len(lnko)):
    oszto *= lnko[i]

print(f"9.: {round(198/oszto)}")

#7.
ossz = 30
legalabb = 21
piros = 1
maradek = legalabb-piros
print(f"7.: {ossz-maradek}")
