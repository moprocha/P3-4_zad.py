#a

user_numbers = []
hit_total = 0

for i in range(6):
    user_numbers.append(int(input("Podaj " + str(i+1) + " liczbę (1-49): ")))

user_numbers.sort()
print(user_numbers)

import random

random_numbers = random.sample(range(1,50),6)

for number in user_numbers:
    if number in random_numbers:
        hit_total += 1


random_numbers.sort()

print(random_numbers)

print("Trafiono", hit_total,"liczb.")

#b

numbers = []
numbers_total = int(input("Podaj liczbę elementów zbioru: "))

for i in range(numbers_total):
    number = int(input("Podaj " + str(i+1) + " element zbioru: "))
    numbers.append(number)

numbers_without_duplicates = []
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)


numbers_without_duplicates.sort(reverse=True)

print(numbers_without_duplicates)

#c

import random

blank_square = "--"
pieces = ["WP", "BP", "BP", "BT", "WQ"]
chessboard = [[blank_square for _ in range(8)]for _ in range(8)]
print(chessboard)
print()
counter = 0

while counter < len(pieces):
    row = random.randint(0,7)
    col = random.randint(0,7)
    if chessboard[row][col] == blank_square:
        chessboard[row][col] = pieces[counter]
        counter += 1

for row in range(len(chessboard)):
    if row == 0:
        print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep = "  ")
    print(row+1, end = " ")
    for col in range(len(chessboard[row])):
        print(chessboard[row][col], end=" ")
    print()
