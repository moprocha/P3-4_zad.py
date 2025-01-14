a = 1
b = 4

print("a = ", a, "b =", b)
temp = a
a = b
b = temp

print("a = ", a, "b =", b)

numbers = [1, 2, 3]
print(numbers)
numbers[0], numbers[1] = numbers[1] , numbers[0]
print(numbers)

# [4, 5, 2, 1]
# [4, 2, 5 ,1]
# [4, 2, 1, 5]
# [2, 4, 1, 5]
# [2, 1, 4, 5]
# [1, 2, 4, 5] -> sortowanie bąbelkowe

numbers = [4, 5, 2, 1]
swapped = True

while swapped:
    swapped = False
    for i in range((len(numbers) - 1)):
        if numbers[i] > numbers [i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            swapped = True
print(numbers)

# wbudowane sortowanie

numbers = [4, 5, 2, 1]
numbers.sort()

print(numbers)

numbers = [4, 5, 2, 1]
numbers.sort(reverse=True)

print(numbers)

numbers = ["C", "A", "", "B"]
numbers.sort()

print(numbers)

numbers = ["C", "A", "", "B"]
numbers.sort(reverse=True)

print(numbers)

list_1 = [9]
list_2 = list_1 #kopiuje nazwę listy a nie jej zawartość (2 nazwy ale 1 lista)
list_2[0] = 13
print(list_1)
print()

list_1 = [9]
list_2 = list_1[:] #kopiuje całą listę
list_2[0] = 13
print(list_1)

# wycinki (slicing)
# lista [start:end]

numbers = [10, 8, 6, 4, 2]
print(numbers)
new_numbers = numbers[1:4]
print(new_numbers)

new_numbers2 = numbers[-4:-1]
print(new_numbers2)

new_numbers3 = numbers[-2:len(numbers)]
print(new_numbers3)

new_numbers4 = numbers[:]
print(new_numbers4)

del numbers[-2:]
print(numbers)

# operatory in, not in

numbers = [1, 2, 3, 4, 5]
print(5 in numbers)
print(6 not in numbers)
print()
# wyrażenia listowe

numbers = [1, 2, 3, 4, 5]
for i in range(1, 101):
    numbers.append(i)
print(numbers)
print()
numbers = [i for i in range(1,101)]
print(numbers)

print()
numbers = [99 for i in range(1,101)]
print(numbers)

print()
numbers = [i**2 for i in range(1,101)]
print(numbers)

print()
numbers = [i for i in range(1,101) if i % 2 == 0]
print(numbers)
#