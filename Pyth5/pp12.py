name = input("Jak masz na imię? ")
print("Witaj {}!".format(name))

# pobranie 3 liczb od uzytkownika i wyswietlenie ich na ekranie

def show_message(number_no):
    print("Proszę podaj liczbę:".format(number_no))

show_message(1)
#print("Podaj liczbę: ")
a = int(input())
show_message(2)
#print("Podaj liczbę: ")
b = int(input())
show_message(3)
#print("Podaj liczbę: ")
c = int(input())

print("Pobrano liczby:", a, b, c)


print("raz", "dwa", "trzy")

def introduce(first_name, last_name):
    print("Cześć, jestem", first_name, last_name + ".")

introduce("Jan", "Kowalski")

introduce (first_name="Julia", last_name="Smith")

print("raz", "dwa", "trzy", sep="-")

def introduce2(first_name="Jan", last_name="Kowalski"):
    print("Cześć, jestem", first_name, last_name + ".")
introduce2("Maciej")

def show_name(name="Jan"):
    print("Cześć, mam na imię {}.".format(name))

show_name("Maciej")
show_name()
print(show_name("Maciej"))
#