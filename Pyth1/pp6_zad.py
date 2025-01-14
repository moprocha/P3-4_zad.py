#a

char=(input("Podak znak: "))
column=int(input("Podak liczbę kolumn: "))
row=int(input("Podak liczbę wierszy: "))


print(((char*column) + "\n")*row)


#b

string_number1 = input("Podaj pierwszą liczbe całkowitą:")
string_number2 = input("Podaj drugą liczbe całkowitą:")

print(int(string_number1)+int(string_number2),int(string_number1)-int(string_number2),int(string_number1)*int(string_number2),int(string_number1)/int(string_number2),int(string_number1)%int(string_number2))

#c
print("+-"*9+ "+")
print(("| "*9 + "|\n") * 1, end="")
print("+-"*9 + "+")

