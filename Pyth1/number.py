string_number = input("Podaj liczbe całkowitą:")
multiplier = 9
print("Gdy liczbę "+ string_number + " pomnożymy przez " + str(multiplier) + " to otrzymamy " + str(multiplier*int(string_number))+".")

#twierdzenie Pitagorasa
a=float(input("Wprowadź długość pierwszego boku: "))
b=float(input("Wprowadź długość drugiego boku: "))

print("Długość przeciwprostokątnej wynosi " + str(round(((a**2+b**2)**0.5),2)))