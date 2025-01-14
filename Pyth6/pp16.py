import math


print(math.pi)
print(math.sin(math.pi/2))

import sys

print(math.factorial(5))
print(math.floor(4.9999))
print(math.sin(234))

# aliasowanie

import math as m

print(m.pi)

from math import pi as PI

print(PI)

from math import pi, sin
import math
print(sin(pi))
print(math.factorial(4))

print()

import math

print(dir(math))
print()

import random

print(random.randint(1,3))

print(random.random()) # od 0 do 1 ale [0.0, 1.0)

from random import random, seed

seed(0) # sprawdzić o co chodzi

for i in range(5):
    print(random())

print()

from random import choice, sample

list = [i for i in range(1,11)]

print(list)
print(choice(list)) # wybiera 1 liczbę ze zbioru
print(sample(list, 5)) # wybiera k liczb ze zbioru bez powtórzeń
print(sample(list, 10))
print()

import platform

help(platform)


print(platform.machine())
print(platform.system())
print(platform.version())
print(platform.release())
print(platform.processor())

print(platform.python_implementation())
print(platform.python_version())
print(platform.python_version_tuple())
#
