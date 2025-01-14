print(0b1101)
print(0o177)
print(1*8*8+7*8+7)
print(1*8**2+7*8**1+7*8**0)
print(0xFFF)
print(15*16**2+15*16+15)

#liczby całkowite

print(2)
print(1_000_000)
print(-2)
print(+2)
print(type(2))

#systemy liczbowe

#dziesiętnie: 123=1*100+2*10+3*1=1*10**2+2*10**1+3*10**0

print(0b101) #literał w systemie dwójkowym
print(0o14) #literał w systemie ósemkowym
print(0xFF) #literał w systemie szesnastkowym

print(0o12+0xA) #10+10

print(type(0o127))

# liczby zmiennoprzecinkowe

print(2.0)
print(2,0)
print(.123)
print(3.)

print(5e3) #5*10**3=5*1000=5000.0
print(1e17)
print(2.45e-4)
print(2.45e-5)

print(123_000_000)
print("{:.2e}".format(123_000_000))
print(2.3e-5)
print("{:.6f}".format(2.3e-5))

#ciąg znaków

print("Ala ma kota, a kot ma Alę.")
print('Ala ma kota, a kot ma Alę.')
print("tekst ze \nznakiem nowej linii")
print("I'm Monty Python")
print('I\'m Monty Python')

print("><", ">\t", ">\t\t\t<", sep="\n")

print("\\\\")

print(type(" "))
print(type(""),"\n")

#wartości logiczne (boolean)

print(False) # z wielkiej
print(2>3)
print(type(2>3))
print(2<9)

print(bool(1))
print(bool(13)) #!
print(bool(0)) #!