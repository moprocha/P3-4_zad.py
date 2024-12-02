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

bits =[]
for n in range(8):
    mask = 1 << n
    result = number & mask
    bit = int(bool(result))
    bits.append(bit)
    n+=1
print(bits)

ones_total = 0
for bit in bits:
    if bit == 1:
        ones_total += 1

if ones_total == 1:
    print("Liczba", number, "ma", ones_total, "jedynkę w ciągu bitów.")
elif ones_total == 2 or ones_total == 3 or ones_total == 4:
    print("Liczba", number, "ma", ones_total, "jedynki w ciągu bitów.")
else:
    print("Liczba", number, "ma", ones_total, "jedynek w ciągu bitów.")

