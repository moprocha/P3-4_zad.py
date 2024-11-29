# wylosuj 3 liczby ze zbioru od 1 do 10 bez powtórzeń, posortuj wynik

#1
import random

random_numbers = []
for i in range(3):
    random_numbers.append(random.randint(1,10))
random_numbers.sort()
print(random_numbers)
print()
import random

#2
random_numbers = []
counter = 3
while counter:
    number = random.randint(1,10)
    if number not in random_numbers:
        random_numbers.append(number)
        counter -=1
random_numbers.sort()
print(random_numbers)
print()
#3

import random

numbers = [i for i in range(1, 11)]
random_numbers = random.sample(numbers, 3)
random_numbers.sort()
print(random_numbers)