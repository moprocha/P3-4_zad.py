# gra toczy sie dopóki nie zostanie odgadnięta liczba

import random

counter = 1
number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (1-10): "))

while guess != number:
    guess = int(input("Nie, to nie ta. Spróbuj jeszcze raz: "))
    counter += 1

print("Brawo! Udało Ci się już za " + str(counter)+" razem.")
#