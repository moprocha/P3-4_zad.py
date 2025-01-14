numbers = []

for i in range(5):
    number = int(input("Podaj liczbę całkowitą: "))
    numbers.append(number)

print(numbers)

# zmiana, zeby zabezpieczyc

numbers2 = []
counter = 1
while True:
    if counter >5:
        break
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        numbers2.append(number)
        counter+=1
    except:
        print("To nie jest liczba całkowita, spróbuj ponownie")

print(numbers2)
#