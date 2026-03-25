dodawanie = lambda x, y: x + y
print(dodawanie(2, 3))

#sortowanie
lista = [6, -9, 3, 0, -12, -1, 7]

#wartość bezwzględna
lista.sort(key = lambda x: abs(x))
print(lista)

#sortowanie po długościach napisów
lista2 = ['matematyka','filozofia','fizyka','informatyka']
lista2.sort(key = lambda x: len(x)) #-len(x)
print(lista2)

#sort wielopoziomowe
ludzie = [['Janusz','Baca'],['Rudolf','Kitler'],['Janek','Baca'],['Sławek','Radek']]
ludzie.sort(key = lambda x: (x[0], x[1]))
print(ludzie)

#liczba dzielników
def dz(liczba):
    ile = 0
    for d in range(1, liczba + 1):
        if liczba % d == 0:
            ile +=1
    return ile
print(dz(12))

lista3 = [12,7,1024,9,16]
lista3.sort(key = lambda x: dz(x))
print(lista3)

#map()
lista4 = [1, 5, -6, 10, -7]
kwadraty4 = list(map(lambda x: x ** 2, lista4))
print(kwadraty4)
#zaawansowane
slownik = {'fiz': 'fizyki'}
fortnite = ['zdaję', 'z', 'fiz']

fort = list(map(lambda x: slownik[x] if x in slownik else x, fortnite))
print(fort)