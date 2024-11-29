#a

numbers = []

i=0
while True:
    char = input("Podaj " + str(i+1) + " liczbę całkowitą:")
    if char == "":
        break
    else:
        numbers.append(int(char))
        i+=1

print("Pobrano następujący zbiór liczb:", str(numbers) + ".")

totalp = 0
totaln = 0
for number in numbers:
    if number % 2 == 0:
        totalp += number
    else:
        totaln += number
print("Suma wszystkich liczb parzystych to", str(totalp), "a nieparzystych", str(totaln) + ".")

print()

#b

import random

lower = int(input("Podaj dolny zakres liczb: "))
higher = int(input("Podaj górny zakres liczb: "))
count = random.randint(lower,higher)

print(count)

random_numbers = []
for i in range(count):
    random_numbers.append(random.randint(lower,higher))
random_numbers.sort() #opcjonalnie

matrix=[random_numbers for count in range(lower,higher)]
print("Wylosowane liczby to: "+str((matrix))+".")
print()

#c

number = int(input("Podaj liczbę całkowitą: "))
print(number)

digits = ["{:8b}".format(number)]
digits2=int(digits[0])
print(digits2)

