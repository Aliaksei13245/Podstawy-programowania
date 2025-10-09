#co można wyświetlać printem
print(5)
print((2 + 2) * 2)

x = 34

print(x)

print('informacja')
print(round(1.23456323432, 2))
print(2 == 3 and 1 > 0)
print([2, 4, 3, 6, 7])

# formatowanie wyswietlania tekstu

imie = input('podaj imie')
nazwisko = input('podaj nazwisko')
wiek = input('podaj wiek')

# sposub 1
'''
print('witaj ' + imie + ' ' + nazwisko + '. masz ' + str(wiek) + 'LAT. Za 5 lat będziesz mieć '
      + str(wiek + 5) + ' lat')
'''
# sposub 2

print(f'Witaj {imie} {nazwisko}. Masz {wiek} lat. Za pięć lat będziesz miec {wiek + 5} lat')

liczba = 4.1234
print(f'Kwota = {liczba: .2f}')

# sposób 3.1
print('Witaj {} {}. Masz {} lat. ZA pięć lat będziesz mieć {} lat.'.format(imie, nazwisko, wiek, wiek + 5))

# sposób 3.2
print('Witaj {1} {0}. Masz {3} lat. ZA pięć lat będziesz mieć {2} lat.'.format(imie, nazwisko, wiek + 5, wiek))
