import random

number = random.randint(1, 3)
guess = int(input("Zgadnij jaką liczbę mam na myśli (1, 2, 3): "))

if guess == number:
    print("Brawo, dokładnie taką liczbę miałem na myśli.")
else:
    print("Niestety, myślałem o liczbie " + str(number) + ".\n")