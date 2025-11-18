'''#jak nie programować wielokrotnie powtarzającej się czynności

a = float(input('podaj liczbe 1'))
b = float(input('podaj liczbe 1'))
c = float(input('podaj liczbe 1'))
d = float(input('podaj liczbe 1'))
e = float(input('podaj liczbe 1'))

suma = (a + b + c + d + e)

print(suma)


suma = 0
liczba = 0

for u in range(0, 5):
    liczba = float(input('podaj liczbę'))
    suma = suma + liczba

print(suma)

#listy
lista = ['qwerty', 56, [6, 7], 4.56, [[5, 8], 1]]
print(lista[2][1])
print(lista[4][0][1])

#listy i pentle
lista2 = ['kot', 'pies', 'owca', 'lama']
for z in lista2:
    print(z)
#pętla for:
#wyciąga dane z list po koleeeeeee
#pentla wyoknuje sie ile elementów pentli

#pentla która sie wykona 3 razy
lista3 = [234, 56, 67]
for i in lista3:
    print('ok')

#pentla 1000 razy
lista4 = [0] * 10
print(lista4)

for i in lista4:
    print('siema')

#generatory i pentle
predzial = range(1, 10) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

for i in predzial:
    print(i)
 #penntla10 razhy
 for i in range(10): #(o, 10)
     print(i)

lista5 = [0]
lista5.append(0)
print(lista5)'''

'''lista6 = [0]

for i in lista6:
    print('hello')
    lista6.append(0)'''

#pentla while

liczba = 10

while liczba > 0:
    print(liczba)
    liczba = liczba - 1