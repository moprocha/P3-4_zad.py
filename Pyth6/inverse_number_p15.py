while True:
    number = (input("Podaj liczbę całkowitą: "))
    if number == "":
        break
    else:
        try:
            number = int(number)
            print("Odwrotna liczba to", 1/number)
        except ValueError:
            print("To nie jest liczba całkowita!")
        except ZeroDivisionError:
            print("Błąd dzielenia przez zero!")
        except:
            print("Coś poszło nie tak...")
#