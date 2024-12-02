#a

numbers = []

for i in range(6):
    numbers.append(int(input("Podaj " + str(i+1) + " liczbę (od 1 do 49):")))
print("Pobrano następujący zbiór liczb:", str(numbers) + ".")
print()

import random

numbers_random_total = 6
numbers_random = []

for i in range (numbers_random_total):
    numbers_random.append(random.randint(1,49))

print("Wylosowane liczby to: " + str(numbers_random) + ".")

common = []
for i in range(6):
    if numbers[i] in numbers_random[:]:
        common.append(numbers[i])

print(common)

print("Ilość trafień to:", str(len(common)) + ".","Trafione liczby to:", str(common)+ ".")

#b

