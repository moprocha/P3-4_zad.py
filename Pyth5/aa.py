def double_print():
    print("Hello")
    print("World")

double_print()

def show_numbers(a,b,c):
    print("a =", a, "b =", b, "c =", c)

show_numbers(1,2,3)

def show_numbers(a,b,c):
    print(a, b, c)

show_numbers(c = 3, a = 1, b = 2)

def introduce(first_name = "Jan", last_name = "Kowalski"):
    print("Cześć, jestem", first_name, last_name + ".")

introduce()

x = None
print(x)

def sum(x, y):
    return x + y
print(sum(1,2))

def generate_numbers(n):
    numbers = []
    for i in range(n):
        numbers.insert(0,i)
    return numbers

print(generate_numbers(5))

def my_func():
    x=3

x=1
my_func()
print(x)

def my_func():
    global x
    x=3

x=1
my_func()
print(x)

def pass_value(a):
    print(a)

pass_value(12)
pass_value([1,2,3])

def show_me_recursion(n):
    if n < 1:
        return
    print("recursion " * n)
    n-=1
    show_me_recursion(n)

show_me_recursion(20)

numbers = [1, 2, 3]
for i in numbers:
    print(i)

numbers = (1, 2, 3)
for i in numbers:
    print(i)