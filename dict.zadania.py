'''zbior = set()
lista2d = [
[5, 2, 8, 5, 1],
[3, 8, 2, 9, 5],
[1, 4, 4, 2, 7],
[6, 3, 9, 1, 4],
[8, 2, 5, 6, 3]
]
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior.add(element)
print(zbior)


zbior_caly = set()
for x in lista2d:
    zbior2 = set(x)
    zbior_caly = zbior_caly.union(zbior2)


lista1d = []
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        lista1d.append(element)
lista_zbior = set(lista1d)
for e in lista_zbior:
    print(e, lista1d.count(e))'''


slowa = [
"LETTER",
"BALLOON",
"SUCCESS",
"HAPPY",
"COFFEE",
"BOOKKEEPER",
"ASSESS",
"MISSISSIPPI",
"ADDRESS",
"TOOLBOX"
]

#slowo = 'lETTER'
#slowo_zbior = set(slowo)
max_lrl = 0
for x in slowa:
    x_zbior = set(x)
    lrl = len(x_zbior)
    if lrl > max_lrl:
        max_lrl = lrl
        max_x = x


#zadanie 2.2
zbior = set()
for x in slowa:
    for y in x:
        zbior.add(y)

for l in zbior:
    lista = []
    for s in slowa:
        if l in s:
            lista.append(s)
    print(f'{l}:{lista}')

