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

'''n = int(input('podaj pow'))
max_napis = ''
for x in range(n):
    napis = input('podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis'''



'''from time import sleep
from random import randint
wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 1000 or wynik2 >= 1000) and abs(wynik1 - wynik2) >= 100):
    akcja += 1
    print(f'Akcja {akcja}')
    #druzyna = int(input('podaj nr drużyny która wygrała'))
    druzyna = randint(1, 2)
    if druzyna == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    sleep(0)

if wynik1 > wynik2:
    print('Drużyna 1')
else:
    print('Drużyna 2')'''



'''liczba = int(input('podaj liczbę'))
    while liczba > 0:
        cyfra = liczba % 10
        liczba = liczba // 10
        print(cyfra, end = '')'''



'''liczba = int(input('podaj liczbę'))
d = 2
ileczyn = 0
ilerczyn = 0
while liczba > 1:
    while liczba % d == 0:
        liczba = liczba // d
        ileczyn += 1
    if liczba % d == 0:
        ilerczyn += 1
    while liczba % d == 0:
        liczba = liczba // ileczyn
        ileczyn += 1
    d += 1
print(ileczyn)'''

from time import sleep
from random import randint
x, y = 0, 0
ruchy = ['a','d','s','w',] * 10 + ['q']
while True:
    #ruch = str(input('podaj kierunrk'))
    ruch = ruchy[randint(0, len(ruchy) - 1)]
    if ruch == 'q':
        break
    elif ruch == 'w':
        if y < 9:
            y += 1
        else:
            print('ruch niemożliwy')
    elif ruch == 's':
        if y > 0:
            y -= 1
        else:
            print('ruch niemożliwy')
    elif ruch == 'd':
        if x < 9:
            x += 1
        else:
            print('ruch niemożliwy')
    elif ruch == 'a':
        if x > 0:
            x -= 1
        else:
            print('ruch niemożliwy')
    print(f'{x}:{y}')
    print(ruch)
    sleep(1)