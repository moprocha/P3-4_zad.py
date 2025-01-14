#a

names = []
total_elemets = int(input("Ile imion chcesz dodac?: "))

for i in range(total_elemets):
    names.append(input("Podaj " + str(i+1) + " imię:" ))
print("Pobrano następujący zbiór imion:", str(names) + ".")

#b

import random

dice_rolls_total = 16
rolls = []

for i in range (dice_rolls_total):
    rolls.append(random.randint(1,6))

print("Zbiór wyników po ", dice_rolls_total, "rzutach kostką" + str(rolls) + ".")
print()
print("Za 8 razem wyrzucono wartość", str(rolls [8-1]) + ".")
print()
sixes_total = 0
for roll in rolls:
    if roll == 6:
        sixes_total += 1
print("Wyrzucono", sixes_total, "razy szóstkę.")
print()
in_row_value_temp = rolls[0]
in_row_total_temp = 0
in_row_value = rolls[0]
in_row_total = 0

for roll in rolls:
    if roll == in_row_value_temp:
        in_row_total_temp += 1
    else:
        in_row_value_temp = roll
        in_row_total_temp = 1
    if in_row_total_temp > in_row_total:
        in_row_value = in_row_value_temp
        in_row_total = in_row_total_temp
print("Pod rząd wyrzucono", in_row_total, "razy wartość", str(in_row_value) + ".") # wypisze taki 1 przypadek, nie więcej!

#c

# ->
# [4,4,1,2,3,4]
# f = [0,0,0,0,0,0,0,0,0,0]
#      0 1 2 3 4 5 6 7 8 9
# f = [0,1,1,1,3,0,0,0,0,0]

digits = [1, 2, 3, 3, 4, 1, 2, 3]
freq = [0,0,0,0,0,0,0,0,0,0]

for digit in digits:
    freq[digit] += 1

print(digits)
print(freq)
print()
most_freq = 0
for i in range(len(freq)):
    if freq[i] > freq[most_freq]:
        most_freq = i
print("Najczęściej występującą cyfrą jest", str(most_freq) + "." + " Wystąpiła", freq[most_freq], "razy.")