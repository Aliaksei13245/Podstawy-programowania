#listy a napisy
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