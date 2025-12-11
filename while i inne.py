'''liczba = 1898864
licznik = 0
while liczba > 0:
    liczba = liczba // 2
    licznik = licznik + 1
    print(liczba)
print(licznik)'''


#zad1
'''x = input('podaj liczbę lub q buy zakończyć')
licznik = 0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('podaj liczbę lub q aby zakończć')'''

'''n = int(input('daj'))
ilczyn = 1
for i in range(n):
    ilczyn = ilczyn + (i + 1)
print(ilczyn)'''

'''wynik = 0
lista = [4, 12, 8, 1, 5, 6, 3]
for i in range(len(lista)):
    for x in range(len(lista)):
        if x != i and (x + i) % 3 == 0:
            wynik += 1
print(wynik)'''

n = int(input('podaj pow'))
max_napis = ''
for x in range(n):
    napis = input('podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
