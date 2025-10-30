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
lista_napisów = ['windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '$'.join(lista_napisów)
print(lista_napisów)
print(całe_zdanie)

lista_napisow2 =['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 ='\n'.join(lista_napisow2)
print(cale_zdanie2)

napis5 = 'prawdopodobieństwo'
ile_razy_o = napis.count('o')
print(ile_razy_o)