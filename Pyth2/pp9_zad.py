#a

range_from = int(input("Podaj dolny zakres liczb: "))
range_to = int(input("Podaj górny zakres liczb : "))

is_first = True
print("Liczby z zakresu od", range_from, "do", range_to, "podzielne przez 3 lub 5 lub 7 to:", end=" ")
for i in range(range_from, range_to+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(", ", end="")
        print(i, end ="")
    is_first = False
print(".")

#b

counter = 0
for i in range(1, 101):
    if ((i % 2 == 0) and (i > 90)) or ((i % 2 !=0) and (i % 9 ==0)):
        counter += 1
print("Tak, to prawda, takich liczb jest " + str(counter) + ".")

#c

number = int(input("Podaj liczbę: "))
n = int(input("Podaj nr bitu: "))

mask = 1 << n
result = number & mask
bit = int(bool(result))

print("Bit na pozycji", n, "dla liczby", number, "wynosi", str(bit) + ".")

print()
# sprawdzenie

print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" *8)
print("{:08b}".format(result))