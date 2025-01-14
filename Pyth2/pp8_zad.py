#a

for i in range(1,101):
    if (i % 3 == 0):
        continue
    print(i, end=" ")
else:
    print("\n")

# lub

for i in range(1,101):
    if i % 3 != 0:
        print(i)

#b

rozm=int(input("Podaj rozmiar: "))
znak=input("Podaj znak: ")

for i in range(1,rozm+1):
    print(znak*rozm, end="\n")

# lub

number = int(input("Podaj rozmiar: "))
char = input("Podaj znak: ")

for i in range(number):
    for j in range(number):
        print(char, end="")
    print()

#c
# 0 1 2 3  4  5...
# 1 2 4 8 16 32..

suma=0
for i in range(64): #bo 64 pola szachownicy
    suma += 2 ** i

print("Suma wszystkich ziaren zboża na szachownicy: " + str(suma))

# założenia: waga 1 ziarna to 0,4 mg, a to jest okolo 0,0004g

# 1kg = 1000g
# 1t = 1000kg

tons = int(suma*0.0004)/1000/1000
print("To będzie", tons, "ton.")

# roczna produkcja pszenicy na świecie to 782 mlns ton

years = int(tons/1_000_000/782)

print("lata: ", years)

# pociąg może przetransportować 2200t
trains = int(tons/2200)

print("pociągów: ", trains)