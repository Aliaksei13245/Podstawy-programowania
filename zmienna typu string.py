napis = 'informatyka'

#Fragment tekstu
#1 wycinanie od  ... do
print(napis[2:5]) # czyli tak naprawdę od 2 do 4 (for)

# wyciananie od .. do co ilieś
print(napis[2:10:2])

# wycinanie od pocczątku
print(napis[:3])

# do końca
print(napis[7:])
# czytanie od końca
print(napis[::-1])

#Zawieranie się znaku w słowie
if 'a' in napis:
    print('należy')
else:
    print('nie należy')

#3 łączenie
napis2 = napis + 'jest najlepsza'
print(napis)

#4 funkcje zmienne typu string

#szukanie danego fragmentu w tekscie
napis3 = 'matematyka'
index_gdzie_jest = napis3.find('ten')
print(index_gdzie_jest)

napis4 = 'alabalalabala'
index_gdzie_jest2 = napis4.find('bala')
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
index_gdzie_jest4 = napis4.find('xyz', index_gdzie_jest2 + 1)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz nie jest w napisie')
else:
    print('xz nie istnieje w napisie')

# podział tekstu na fragmenty
'''piec_liczb = input('podaj piec liczb. odziel je przcinkami')
piec_liczb_po_podziale = piec_liczb.split(',')
print(piec_liczb_po_podziale)
trzecia_liczba = int(piec_liczb_po_podziale[2])
print(trzecia_liczba)'''

# łączenie napisów
lista_napisow = ['windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '$'.join(lista_napisow)
print(lista_napisow)
print(cale_zdanie)

lista_napisow2 =['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 ='\n'.join(lista_napisow2)
print(cale_zdanie2)

napis5 = 'prawdopodobieństwo'
ile_razy_o = napis.count('o')
print(ile_razy_o)

#5.) "Mutowalnosc stringów"
napis6 = 'fiwyka'
'''napis6[2] = '2'''
#wniosek: stringi nie są mutowalne

#dobry sposób na mutowanie
napis6_lista = list(napis6)
napis6_lista[2] = 'z'
napis6_gotowy = ''.join(napis6_lista)
print(napis6_gotowy)

#Długość napisu
napis7 = 'językpolski'
# .isalpha() == True  .isdigit() == True   .isalnum == True
#       litery       /       cyfry       /   cyfry lub litery

print(len(napis7))

#7 powilanie stringów
napis8 = 'informatyka'

#9 kody ASCII
#9.1 ze znaku na kod ASCII
print(ord('A'))

#9.2 z kodu ASCII na znak
print(chr(66))

#10 funkcja translate
slownik = str.maketrans('ąęćżłśńóź!', 'aeczlsnoz?')
napis12 = 'ińfórmątyką!'
napis12poprawny = napis12.translate(slownik)
print(napis12poprawny)

#11 funkcje dużych i małych liter
napis13 = 'KoNgO'
napis13_dyze = napis13.upper()
print(napis13_dyze)

napis14 = 'KoNgO'
napis14_male = napis13.lower()
print(napis14_male)

#12 podstawianie ciągów znaków
napis15 = 'Chleb kosztuje 15 zł, a bułken 5 zł'
napis15_w_euro = napis15.replace('zł', '$')
print(napis15_w_euro)

#13 sortowanie i odwracanie napisu
# odwracanie
napis14 = 'kemot'
napis14_od = napis14[::-1]

#sortowanie
napis16 = 'dbca'
napis16_posortowany = sorted('napis16')
napis16_posortowany_wynik = ''.join(napis16_posortowany)
print(napis16_posortowany_wynik)

