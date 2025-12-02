#zadanie 15
'''X = list(range(0, 103, 3))
print(f'x\ty')
for x in X:
    y = 0.5 * x + 3
    print(f'{x}\t{y}')
print(f'x\ty')
for x in range(0, 103, 3):
    y = 0.5 * x + 3
    print(f'{x}\t{y}')'''

#b
'''print(f'x\t\ty')
for x in range(-30, 61):
    X = x / 10
    y = 0.5 * x + 3
    print(f'{x}\t{y}')'''

#16
'''lista1 = list(range(3, 31, 3))
lista2 = list(range(11, 111, 11))
lista3 = list(range(13, 131, 13))

#sposób 1
for x, y, z in zip(lista1, lista2, lista3):
    print(f'{x}\t{y}\t{z}')
lista10 = [15, 23, 34, 52]
#sposób 2
for i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')
for i in lista10:  # k zawiera elementy
     print(i)

    # chodzenie po liscie indeksami - liczymy od zera

for k in range(0, 4): # range(0) k jest indeksem
    print(lista10[k])
    
for k in range(len(lista10)):#len to długość listy
    print(lista10[k])'''

from math import inf
# inf to bardzo wielka liczba
#17
suma = 0
n = int(input('podajile będzie liczb'))
max_liczba = -inf #minus nieskńczoność
min_liczba = inf # plud nieskończoność

for x in range(n):
    liczba = int(input('podaj liczbę'))
    suma = suma + liczba
    if liczba > max_liczba:
        max_liczba = liczba
    if liczba < min_liczba:
        min_liczba = liczba
print(suma)
print(suma / n)
print(max_liczba)
print(min_liczba)

'''lista = [7]
for i in lista:
    liczba = float(input('podaj liczbe rzeczewista'))
    print(liczba)
    if liczba != 0:
        lista.append(3)'''

'''a = 1
while a > 1:
    print(a)
    a.append(1)'''

'''lista = [3, 4, 4, 3, 7, 8, 9,]
for i in range(len(lista)):
    print(lista[i])'''
'''x = 1
a = 1
while a > 0:
    print(x)
    x += 1
    a += 1'''

'''a = [1]
a.append()
print(a)'''

'''lista = [1]
for i in lista:
    print('hello')
    lista.append(1)
'''

'''lista = [1, 3]
lista += [1]
print(lista)'''
print(sum(x))