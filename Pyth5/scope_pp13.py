def scope_test(): #zmienna lokalna
    print("w srodku funkcji:", x)


x = 123 # zmienna globalna
scope_test()
print("poza funckja", x)

def scope_test():
    x = 999 # zmienna lokalna, nadpisała zmienną globalną
    print("w srodku funkcji:", x)


x = 123 # zmienna globalna
scope_test()
print("poza funckja", x)
#