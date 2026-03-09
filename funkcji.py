'''def hurra():
    print('Hurra!\n' * 50)

#n to parametr
#6 argument funkcji
#hurra2(6) to wywołanie funkcji
def hurra2(n):
    print('Hurra!\n' * n)

hurra2(6)

def hurra3(n = 10):
    print('Hurra!\n' * n)

hurra3()

#jeżeli funkcja poprostu wykonuje jakąś czynność i nie możemy wykożystać efektów jej pracy wtedy to jest procrdura

#pole całkowite graniastosłupa prawidłowego równobocznego

def p_tr_rown(a):
    return a ** 2 * (3 ** 0.5) / 4


#Pp = p_tr_rown(3 ** 0.25)

def p_prst(a, b):
    return a * b
#Psb = p_prst(5, 4)

def p_gran_praw_troj(a, b):
    return 2 * p_tr_rown(a) + 3 *p_prst(a, b)
Pg = p_gran_praw_troj(6, 4)
print(Pg)'''


#Zad 0.3 A
'''def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w
u = [2, 7, 3]
v = [-1, 0, 4]

wynik = suma_v(u, v)
print(wynik)

def iloczyn_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] * v[i]
        w.append(suma)
    w = sum(w)
    return w
u = [2, 7, 3]
v = [-1, 0, 4]

wynik = iloczyn_v(u, v)
print(wynik)
'''
#1
'''def czy_anagramy(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
print(czy_anagramy('nosek', 'keson'))

#2
s1 = 'nosek'
s2 = 'keson'
print(sorted(s1) == sorted(s2))'''

#

'''def jaki_tr(a, b, c):
    if a ** 2 + b ** 2 + c ** 2 == 2 * max([a, b, c]) ** 2:
        print('prostokątny')
jaki_tr(1, 2, 3)'''


'''def ilecyfr(liczba):
    licznik = 0
    while liczba  > 0:
        liczba = liczba // 10
        licznik += 1
    return licznik

print(ilecyfr(127))'''

def unikatowe_elementy(l1, l2):
    zbior = set()
    l = l1 + l2
    for x in l:
        if l.count(x) == 1:
            zbior.add(x)
    return zbior

print(unikatowe_elementy([1,2,3,4,5], [1,3,5,6]))


