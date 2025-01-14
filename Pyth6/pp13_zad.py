#a
import string

exp = int(input("Podaj potęgę liczby: "))

def power_numbers(numbers, exp):
    numbers = numbers[:] # zabezpieczenie przed modyfikacją listy
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**exp
    return numbers

numbers = [1,2,3,4,5]


print(power_numbers(numbers, exp))

# lub

def pow2(numbers, exp):
    result = []
    for n in numbers:
        result.append(n**exp)
    return result

numbers = [1,2,3,4,5]

print(pow2(numbers, exp))

# lub

def pow3(numbers, exp):
    return [x ** exp for x in numbers]

print(pow3(numbers, exp))

#b

# 1 x 1 = 1

def show_op(a,b):
    print(a, "x", b, "=", a*b)
    if a == 10 and b == 10:
        return
    elif a == 10:
        show_op(1, b+1)
    else:
        show_op(a+1, b)


show_op(1,1)


#c

import random

# ["A", "B", "C"]

# kod znaku a to 65 -> ord("A")

def draw_letter():
    return chr(random.randint(ord("A"), ord("E")))

def draw_row():
    return [draw_letter() for _ in range(3)]

def check(row):
    if row[0] == row[1] == row[2]:
        return True
    else:
        return False

# do jakiego momentu bedzie false, i w koncu da true?

counter = 1

while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1

print(ord("A")) # -> odwrotna chr(65)
print(chr(65))
print()
print(draw_letter())
print(draw_row())
print(check(draw_row()))
print()

# większa liczba liter

first_symbol = "A"
last_symbol = "D"
number_of_letters = 15

def draw_letter():
    return chr(random.randint(ord(first_symbol), ord(last_symbol)))

def draw_row():
    return [draw_letter() for _ in range(number_of_letters)]

def check(row):
    first_element = row[0]
    for element in row:
        if first_element != element:
            return False
        return True

# do jakiego momentu bedzie false, i w koncu da true?

counter = 1

while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1

print(ord("A")) # -> odwrotna chr(65)
print(chr(65))
print()
print(draw_letter())
print(draw_row())
print(check(draw_row()))

#