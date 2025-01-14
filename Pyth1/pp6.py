print(2+2)
print("2"+"2")
print("2"+"2")
print("3"+"2")
print("2"+"3")

#konersja typów

number = int("2") # ze stringa
print(number+2)

temp = float("36")
print(temp)

temp = float("36.")
print(temp)

age = 24
print("Mam", age, "lata.")
print("Mam " + str(age) + " lata.")

age1 = str(24)
print("Mam", age1, "lata.")
print("Mam " + age1 + " lata.")

# operator replikacji

print("Ala" *3)
print(3*"Ala")

# print("Ala"+3) -- da błąd

print("+" + 10 * "-" + "+")
print(("|" + 10 * " " + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")