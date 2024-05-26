with open('./input.txt', 'r') as f:
  input = f.read().lower().replace(" ", "")

darabok = []
darabok = input.split("\n")
alfanumerikus = "abcdefghiklmnopqrstvxyz0123456789"
print(darabok)

egyezesek = []
egyedik = []
for i in range(len(darabok)):
  y = darabok[i]
  egyezes = 0
  x = ""
  egyedi = ""
  egyedi_db = 0
  for i in range(len(y)):
    if y[i] in alfanumerikus:
      x += y[i]

  for i in range(len(x)-1):
      if x[len(x) - (i + 1)] == x[i]:
        egyezes += 1
  egyezesek.append(egyezes)

  for i in range(len(x)):
    if x[i] not in egyedi:
      egyedi += x[i]
      egyedi_db += 1
  egyedik.append(egyedi_db)
print(egyezesek)  # 28
print(egyedik)

palindrom_e = []
for i in range(len(egyezesek)):
  if egyezesek[i] == (len(darabok[i])-1):
    palindrom_e.append("YES")
  else:
    palindrom_e.append("NO")
print(palindrom_e)

for i in range(len(darabok)):
  print(f"{palindrom_e[i]}, {egyedik[i]}")
