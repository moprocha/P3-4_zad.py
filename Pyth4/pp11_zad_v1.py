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
print()
#b

numbers = []

i=0
while True:
    char = input("Podaj " + str(i+1) + " liczbę całkowitą:")
    if char == "":
        break
    else:
        numbers.append(int(char))
        i+=1
numbers.sort(reverse=True)
print("Pobrano następujący zbiór liczb:", str(numbers) + ".")
print(numbers)

numbers2 = []
for j in range(len(numbers)):
    if numbers[j] not in numbers2:
        numbers2.append(numbers[j])
        #j += 1

print("Liczby bez duplikatów to:", str(numbers2)+ ".")

#c

import random

chess_row = ["--" for _ in range(8)]
print(chess_row)
print()
chessboard = [["--" for _ in range(8)] for _ in range(8)]
print(chessboard)
print()
chessboard [random.randint(0,7)][random.randint(0,7)] = "FS"
chessboard [random.randint(0,7)][random.randint(0,7)] = "FS"
chessboard [random.randint(0,7)][random.randint(0,7)] = "PI"
chessboard [random.randint(0,7)][random.randint(0,7)] = "PI"
chessboard [random.randint(0,7)][random.randint(0,7)] = "PI"

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()
#