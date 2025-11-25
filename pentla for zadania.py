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

#17
suma = 0
n = int(input('podajile będzie liczb'))
for i in range(n):
    liczba = int(input('podaj liczbę'))

    for a in range(liczba + 1):
        suma = suma + a
print(suma)


