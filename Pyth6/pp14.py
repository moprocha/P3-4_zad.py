numbers = [1,2,3]
tuples = (1,2,3) # krotka

print(tuples)

numbers = ()
print(numbers)

for number in numbers:
    print(number)

numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)
print()
numbers = tuple(x for x in range(10) if x % 2 == 0)
print(numbers)
print()
numbers = list(x for x in range(10) if x % 2 == 0)
print(numbers)

numbers = (1,2,3)

#numbers[0] = 999 # nie mozna modyfikowac krotki

#del numbers[0] # nie mozna usuwac elementu krotki

#del numbers # cala krotke mozna usunac
print(numbers)

numbers2 = (1,2,3)

print(len(numbers2))
print(numbers2*2)

numbers3 = [1,2.3]

print(numbers3, type(numbers3))

numbers4 = (1,2.3)

print(numbers4, type(numbers4))

letters = tuple('abc')
print(letters)
print()
phones = {"Tomek": 123456789, "Ada": 987654321, "Karol": 789456123}
print(phones)
print()

animals_dict = {
    "kot":"cat",
    "pies":"dog",
    "chomik":"hamster"
}
print(animals_dict)
print(animals_dict["kot"]) # wg klucza
print(animals_dict.get("kot")) # to samo
print(animals_dict.get("wiewiórka", "brak klucza w słowniku")) # nie ma takiego elementu + informacja
print(animals_dict.get("pies", "brak klucza w słowniku"))
print()
words = ["kot", "lew","chomik"]

for word in words:
    if word in animals_dict.keys():
        print(word, "->", animals_dict[word])
    else:
        print("Nie znaleziono słowa {} w słowniku".format(word)+".")
print()

for key in animals_dict:
    print(key, "->", animals_dict[key])
print()

for value in animals_dict.values():
    print(value)
print()

for item in animals_dict.items(): # krotka/lista krotek
    print(item)
print()

for key, value in animals_dict.items():
    print(key, value)
print()

for pl, en in animals_dict.items():
    print(pl, "->", en)

# modyfikacja słownika

animals_dict["świnka"] = "pig"  # dodanie na koncu
print(animals_dict)
print()

animals_dict.popitem() # usuniecie ostatiego elementu
print(animals_dict)
print()

animals_dict.clear() # usunięcie całego słownika
print(animals_dict)
#
