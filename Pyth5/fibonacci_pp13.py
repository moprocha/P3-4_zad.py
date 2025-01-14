# ciąg Fibonacciego
# 1 1 2 3 5 8 13 ...

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    sum = 0

    for i in range(3, n+1):
        sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, sum

    return sum

for n in range(1,50):
    print(n, "->", fib(n))

print()
print(fib(6))
print()
# sposób 2: rekurencja

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    return fib(n-1) + fib(n-2)  # fib(2) + fib(1) -> 1 + 1 -> 2
                                # fib(3) + fib(2) -> 2 + 1 -> 3

for n in range(1,11):
    print(n, "->", fib(n))
#