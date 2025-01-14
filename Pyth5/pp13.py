# zsumuj wszystkie elementy listy

def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

numbers = [1,2,3,4,5]
print(sum_numbers(numbers))

# wylosuj dowolna liczbe liczb od 1 do 99

import random

def generate_numbers(total_numbers):
    numbers = []
    for _ in range(total_numbers):
        numbers.append(random.randint(1, 99))
    return numbers

print(generate_numbers(10))
print(generate_numbers(100)) # sprawdzic nagranie!!
#
