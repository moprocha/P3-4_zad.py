# pobieramy od użytkownika długości 3 odcinków
# sprawdź, czy można z nich zbudować trójkąt
# sprawdź, jaki to będzie trójkąt ze względu na boki (różnoboczny, równoboczny, równoramienny)
# sprawdź, jaki to będzie trókąt ze względu na kąty (prostokątny, ostrokątny, rozwartokątny)

print("Podaj długości 3 odcinków (liczby całkowite)")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a+b>c and a+c>b and b+c>a:
    print("Z tych odcinków można zbudować trójkąt.", end=" ")
    if a==b and a==c and b==c: #a==b==c
        print("Trójkąt jest równoboczny.", end =' ')
    elif a==b or a==c or b==c:
        print("Trójkąt jest równoramienny.", end=' ')
    else:
        print("Trójkąt jest róźnoramienny.", end=' ')
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("Trójkąt jest prostokątny.", end=' ')
    elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or c ** 2 + a ** 2 < b ** 2:
        print("Trójkąt jest rozwartokątny.", end=' ')
    else:
        print("Trójkąt jest ostrokątny.", end=' ')
else:
    print("Z tych odcinków nie powstanie trójkąt.")



