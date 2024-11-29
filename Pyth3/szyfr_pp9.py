# rozszyfruj wiadomość
# szyfr: dla każdego znaku zmieniono 4 bit na przeciwny
# bity liczymy od najmniej znaczącego

msg = "Xq|`gf(bm{|(nibfq)"

# funkcja - pokazuje numer znaku w systemie z tabeli ASCII

print(ord("c"))

# w drugą stronę

print(chr(99))

print("{:08b}".format(ord("c")))

# maskowanie bitów

# 01100011 -> chcemy zmienić 4 bit (od prawej)
# 00001000 - tylko 4ty bit
# korzystamy z XOR (alternatywa rozłączna)
# 01101011
# przesunąć w lewo 1 o 3 pozycje => (1<<3)

print("{:08b}".format(1<<3))
print("{:08b}".format(ord("c") ^ (1<<3)))
print()
for c in msg:
    n=ord(c) ^ (1<<3)
    print(chr(n), end="")

