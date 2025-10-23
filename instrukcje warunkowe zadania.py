#rozwiązywanie równania kwadratowego
'''
a = float(input('podaj a różną od zera'))
b = float(input('podaj b'))
c = float(input('podaj c'))

delta = b ** 2 - 4 * a * c
if delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print(f'x1 = {x1} v x2 = {x2}')
elif delta == 0:
    x = (-b) / (2 * a)
    print('x1 = x2 = {}'.format(x))
else:
    print('brak rozwiązań')
'''

#zadnie 12
pisemny_j_polski = int(input('pisemny polski'))
pisemny_j_obcy = int(input('pisemny obcy'))
dodatkowy = int(input('dodat.'))
ustny_j_polski = int(input('ustny polski'))
ustny_j_obcy = int(input('ustny obcy'))

if pisemny_j_polski >= 30 and pisemny_j_obcy >= 0 and dodatkowy >= 30 and ustny_j_polski >= 30 and ustny_j_obcy >= 30
    print('not amnestiqa')
elif (pisemny_j_polski + pisemny_j_obcy + dodatkowy + ustny_j_polski + ustny_j_obcy) / 5 >= 30:
    print('zdałeś z amnestią')
elif:
    print('nie zdałeś')