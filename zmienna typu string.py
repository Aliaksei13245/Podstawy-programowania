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