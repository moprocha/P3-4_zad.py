# 5 or 7

print(5 or 7) # sprawdza tylko 1 element i kończy
print(5 and 7) # sprawdza drugi element, bo jest to konieczne
print()
print(1)
print(print(1))
print()
print(print(1) or print(2))
print()
print(print(1) and print(2))

print()

a=3
b=2
c=11
d=2
e=20

print(a,b,c,d,e)

numbers = [3,2,11,2,20]
print(numbers)

fruits =['apple','pear','orange','banana']
print(fruits)

# własności list
# - jest uporządkowana

numbers = [1, 2, 3]
print(numbers)

# pozwala przechowywać duplikaty

numbers = [1, 1, 1]
print(numbers)

# pozwala na przechowywanie elementów o różnych typach
numbers = [1, "jeden", True, 2.0, 9]
print(numbers)

# - każdy element z listy posiada indeks
# - elementy z listy są zawsze numerowane od 0

print(numbers[0], numbers[1])

#           0       1       2        3
fruits = ['apple','pear','orange','banana']
print(fruits[2])

#           -4      -3      -2      -1
print(fruits[-2])

# używamy list do przechowywania wiadomości w wyprodukowanych monetach
denver = [1_700_000, 4_600_000, 2_100_000]
philadelphia =[]
philadelphia.append(1_800_000)
philadelphia.append(5_000_000)
philadelphia.append(2_500_000)
print(denver)
print(philadelphia)

total = [0, 0, 0]
total[0] = denver[0] + philadelphia[0]
total[1] = denver[1] + philadelphia[1]
total[2] = denver[2] + philadelphia[2]
print(total)

average = (total[0] + total[1] + total[2])/len(total)
print(average)
print("Produkcja w 2012 roku wyniosła", "{:,d}".format(total[0]).replace(","," "), "sztuk.")
print("Produkcja w 2013 roku wyniosła", "{:,d}".format(total[1]).replace(","," "), "sztuk.")
print("Produkcja w 2014 roku wyniosła", "{:,d}".format(total[2]).replace(","," "), "sztuk.")
print("Średnia produkcja wyniosła", "{:,.0f}".format(average).replace(","," "), "sztuk.")
print()

fruits =['apple','pear','orange','banana']
print(fruits)
print(len(fruits), fruits)

del fruits[0]
print(fruits)
print(len(fruits), fruits)

del fruits
print(len(fruits))
print(fruits[0])

