'''#listy a napisy
napis = 'informatyka'
lista = list(napis)
print(lista)

#zamiana napisu na listie

#zakres i lista
zakres = range(3, 10, 2)
lista2 = list(zakres)
print(lista2)

#indeksowanie elementów listy
lista3 = [1, 'osa', 34, [2, 3, 7, 8], 5, 43]
print(lista3[1:3])#wycinanie fragmentu listy
print(lista3[3][2]) #obsługa listy zagniezdżonej
print(lista3[3][::2])
#4 powielanie listy
#dodawanie list
lista4 = ['a', 34, 56]
lista5 = [[4, 8], 56, 12]
lista6 = lista5 + lista4

#dodawanie list 2
lista7 = ['a', 34, 56]
lista8 = [[4, 8], 56, 12]
lista8.extend(lista7)
print(lista8)

#mnożenie listuy przez liczbę
lista9 = [0] * 1000
print(lista9)
lista10 = [[0] * 10] * 10
lista10[0][0] = 5
print(lista10)

#sortowanie i odwracanie listy
lista11 = [1,5,3,9,7,54,75,3,25,65,6]
#lista11.sort()
lista11.reverse()
print(lista11)
#yrażenia listowe/listy składane
lista12 = list(range(1,11))
lista12_kwadraty = [x ** 2 for x in lista12 if x % 2 == 0]
print(lista12_kwadraty)

#usuwanie z listy

#usuwamie elementu na bazie jego wartosc
lista11.remowe(4) #pierwsze od lewej
while 4 in lista12:
    lista12.remove(4)

#na bazie indeksu
del lista11[2] # el. o indeksie 2'''



'''lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'śledź', 'pstrąg']]

#a
print(lista2[1][2])

#b
mrowka = list(lista2[3])

#odwrotnie
slowo = ''.join(mrowka)
print(slowo)

#c
lista3 = lista1[2::2]
print(lista3)

#d
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_a.append(lista_b)
print(lista_a)
lista2.append(lista2[1] * 3)
print(lista2)

#e
lista1 = lista1 + [9, 6, 16, -8, 7]
print(lista1)

#f
#lista1.sort()
lista1_p = sorted(lista1)
print(lista1_p)
print(lista1_p[0], lista1_p[-1])
print(min(lista1),max(lista1))

#g
del lista1[4]
print(lista1)

#h
del lista1[4:9]

#g
while 2 in lista1:
    lista1.remove(2)

lista1 = [x for x in lista1 if x != 2]
#lista3 =  [x ** 2 for x in lista1]
lista3 = []
for x in lista1:
    lista3.append(x ** 2)
print(lista3)'''



'''lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]
x_max = max(lista)
x_min = min(lista)
lista_norm = [(x - x_min) / (x_max - x_min) for x in lista]
print(lista_norm)'''

#Zadanie 13
lista = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]
#lista = [x for x in lista if x < 1000 or x > 9999]
lista = [x for x in lista if not (x >= 1000 and x <= 9999)]

oceny = {'matematyka': 3,'fizyka': 2,'polski': 4}
#dostawanie się do wartości pod danym kluczem
print('fizyka')#pobieramy wartość ze słownika

oceny['polski'] = 5

#dodawanie klucza do słownika
oceny['geografia'] = 6
print(oceny)
zbior = {}
#sklejanie słownika z listy kluczy i wartości
klucze = ['Bitwa pod Grunwaldem', 'chrzest Polski', 'III rozbiór Polski']
wartosci = [1410, 966, 1795]
for i in range(len(klucze)):
    zbior[klucze[i]] = wartosci[i]
print(zbior)
slownik = dict(zip(klucze, wartosci))
print(slownik)

slownik2 = dict(janisz = 21, alojzy = 99, Bracislawa = 67)
print(slownik2)

del oceny['fizyka']
print(oceny)

for k in oceny:
    print(k, oceny[k])

for i in oceny.items():
    print(i)
