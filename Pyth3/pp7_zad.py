#a

number = int(input("Podaj liczbę: "))
print("Liczba ")

if number**(1/2) % 1 == 0:
    print(" - całkowita")
else:
    print(" - nie jest całkowita")

# lub

number = int(input("Podaj liczbę: "))

if number**(1/2) % 1 == 0:
    str1 = "Tak"
    str2 = ""
else:
    str1 = "Nie"
    str2 = "nie "

print(str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + "jest liczbą całkowitą." )

#b

points = int(input("Podaj ilość punktów otrzymanych przez studenta na kolokwium (0-100): "))

print("Twoja ocena jest ", end="")
if points >= 95:
    print("bardzo dobra (5,0).")
elif points > 84:
    print("ponad dobra (4,5).")
elif points >= 70:
    print("dobra (4,0).")
elif points > 60:
    print("dość dobra (3,5).")
elif points > 50:
    print("dostateczna (3,0).")
else:
    print("niedostateczna (2,0).")

#c

import random

number = random.randint(1, 10)
msg = "Zgadnij liczbę z przedziału od 1 do 10: "
guess = int(input(msg))

if guess == number:
    print("Brawo, dokładnie taką liczbę miałem na myśli!")
else:
    msg = "Masz kolejna szansę, moja liczba jest "
    if number % 2 == 0:
        msg += "parzysta: "
    else:
        msg  += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Udało sie odganąć już za 2 razem!")
    else:
        msg = "Masz ostatnią szansę, moja liczba jest "
        if number >5:
            msg += "większa niż "
        else:
            msg += "mniejsza lub równa "
        msg += "pięć: "
        guess = int(input(msg))
        if guess == number:
            print("Brawo! A jednak do 3 razy sztuka!")
        else:
            print("Niestety, myślałem o liczbie " + str(number) + ".")
#

