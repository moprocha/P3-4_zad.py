#a
import platform

print("Procesor tego komputera to:", platform.machine()+ str("."))

import random

list = [i for i in range(1,11)]

print("Wylosowane 3 niepowtarzające sie liczby ze zbioru od 1 do 10 to:", str(random.sample(list,3)) + str(".") )

import math

print("Sinus kąta 90 stopni to:", str(math.sin(math.pi/2)) + str("."))
#
