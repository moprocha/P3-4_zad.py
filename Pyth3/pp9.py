temp =  12
is_sun_shining = False

if temp > 0 and is_sun_shining:
    print("Idziemy na spacer.")
else:
    print("Zostajemy w domu.")

temp =  12
is_sun_shining = True

if temp > 0 and is_sun_shining:
    print("Idziemy na spacer.")
else:
    print("Zostajemy w domu.")

print("-" *20)

# jeżeli będzie ujemna temperatura lub będzie pochmurnie to...
# zostaniemy w domu, a jeżeli nie, to pójdziemy na spacer

temp =  12
is_sun_shining = False

if not (temp < 0 or not is_sun_shining):
    print("Idziemy na spacer.")
else:
    print("Zostajemy w domu.")

# operatory logiczne
# and - koniunkcja - czytamy jak i
# or - alternatywa - czytamy jak lub
# not - negacja - czytamy jak nie

# iterujemy od 0 do 9 (10 iteracji)
# wyświetlamy cyfrę chyba, że...
# liczba parzysta lub liczba większa od 6 to wyświetl *

for i in range(10):
    if i % 2 == 0 or i > 6:
        print("*")
    else:
        print(i)

# łańcuchowe operatory porównania

a, b, c = 2, 3, 4

if a<b and b<c:
    print("!!!")

if a < b < c:
    print("!!!")

if 5 or 6: # True OR True
    print("OK")

print("-" *20)

a = 5
b = 3

# koniunkcja bitowa
print(a, "&", b, "=", a&b)
print(bin(a)) # binarny skrótem

print("{:08b}".format(a)) # binarny pełny
print("{:08b}".format(b))
print("-"*8)
print("{:08b}".format(a&b))

# alternatywa bitowa

print(a, "|", b, "=", a|b)

print("{:08b}".format(a)) # binarny pełny
print("{:08b}".format(b))
print("-"*8)
print("{:08b}".format(a|b))

# alternatywa rozłączna

print(a, "^", b, "=", a^b)

print("{:08b}".format(a)) # binarny pełny
print("{:08b}".format(b))
print("-"*8)
print("{:08b}".format(a^b))

# przesunięcie bitowe w prawo

print(a, ">>", b, "=", a>>b)

print("{:08b}".format(a)) # binarny pełny
print("-"*8)
print("{:08b}".format(a>>b))

# przesunięcie bitowe w lewo

print(a, "<<", b, "=", a<<b)

print("{:08b}".format(a)) # binarny pełny
print("-"*8)
print("{:08b}".format(a<<b))

# negacja bitowa

print("~" +str(a), "=", ~a)

print("{:08b}".format(a)) # binarny pełny
print("-"*8)
print("{:08b}".format(~a))

print("~" +str(b), "=", ~b)

print("{:08b}".format(b)) # binarny pełny
print("-"*8)
print("{:08b}".format(~b))

print(~1)
# 00000001 (1) => 11111110 (-2)
print(~222)
print(~-255)

for i in range(5, -6, -1):
    print("{0:08b} +> {1:d}".format(i , i))
print()
for i in range(5, -6, -1):
    print("{0:08b} +> {1:d}".format(i & 255, i))

