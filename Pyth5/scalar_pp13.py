def change_value(n):
    print("przed zmianą:", n)
    n+=1
    print("po zmianie", n)

value = 7
change_value(value)
print(value)

def change_value(my_list_1):
    my_list_1 = [0,0]

my_list_2 = [1,2]

change_value(my_list_2)
print(my_list_2)

def change_value(my_list_1):
    my_list_1[0] = 999

my_list_2 = [1,2]

change_value(my_list_2)
print(my_list_2)
#