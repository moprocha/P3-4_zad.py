#a

imie = "Adam"
wiek = 23
miasto = "Kraków"

print("Pan", imie, "ma", wiek, "lat i pochodzi z miejscowości", miasto+".\n")
print("Pan " + imie +" ma "+ str(wiek) + " lat i pochodzi z miejscowości " + miasto+".\n")

#b

a = 2
b = 7
c = 11
d = 19

print ("Pole powierzchni kwadrata wynosi", a*a,",obwód kwadrata wynosi",4*a,",długość przekątnej kwadrata wynosi",round(((2*a**2)**0.5),2),".\n") # a*2**0.5
print ("Pole powierzchni kwadrata wynosi", b*b,",obwód kwadrata wynosi",4*b,",długość przekątnej kwadrata wynosi",round(((2*b**2)**0.5),2),".\n")
print ("Pole powierzchni kwadrata wynosi", c*c,",obwód kwadrata wynosi",4*c,",długość przekątnej kwadrata wynosi",round(((2*c**2)**0.5),2),".\n")
print ("Pole powierzchni kwadrata wynosi", d*d,",obwód kwadrata wynosi",4*d,",długość przekątnej kwadrata wynosi",round(((2*d**2)**0.5),2),".\n")

#c

L = 46_567.
r = 7.5/100
print("Zysk z lokaty po 3 latach wynosi",round((((L*(1+r))*(1+r))*(1+r) - L),2),"zł.")

L1 = 46_567.
d=(1+r)
L1=L1*d
L1*=d
L1*=d
print(round((L1-L),2))