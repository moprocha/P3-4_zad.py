#a
def show_char(char="*", repeat = 10, vertical = False):
    for i in range(repeat):
        if vertical:
            print(char)
        else:
            print(char + " ", end="")
    if not vertical:
        print()
    print()

show_char()
show_char(char="?", repeat=5, vertical=False)
show_char(char="^", repeat=10, vertical=True)
show_char()

#b
def perimeter(a, b):
    return 2*a+2*b

result = perimeter(4,5)
print(result)

result = perimeter(2673,5578)
print(result)

result = perimeter(344555,788998)
print(result)
print()
def area(a, b):
    return a*b

result = area(4,5)
print(result)

result = area(2673,5578)
print(result)

result = area(344555,788998)
print(result)
print()
def diagonal(a, b):
    return (a**2+b**2)**0.5

result = diagonal(4,5)
print(round(result,2))

result = diagonal(2678,5678)
print(round(result,2))

result = diagonal(344555,788998)
print(round(result,2))
print()
def show_result(a, b):
    print("Prostokąt o bokach {} i {}:".format(a, b))
    print("Obwód:", perimeter(a,b))
    print("Pole powierzchni:", area(a,b))
    print("Długość przekątnej:", diagonal(a,b))
    print()

show_result(4,5)
show_result(2678,5678)
show_result(344555,788998)

#c

print("Obliczenie wskaźnika BMI:")
def bmi(waga, wzrost):
    return waga/(wzrost**2)*10_000


b=int(input("Podaj wzrost:"))
a=int(input("Podaj wagę:"))

result = bmi(a,b)
print(result)

print("-----")

weight_in_kg = float(input("Podaj swoją wagę w kg: "))
height_in_cm = float(input("Podaj swój wzrost w cm: "))

def calc_bmi(weight_in_kg, height_in_m):
    return weight_in_kg/(height_in_m)**2

print(calc_bmi(90, 1.8))

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

bmi = calc_bmi(weight_in_kg,height_in_cm * 0.01)
category = determine_bmi_category(bmi)

print("Wskaźnik BMI:", round(bmi,2))
print("BMI Category:", category)
#