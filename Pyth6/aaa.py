print('Funkcja pierwsza zwracająca ile puszek jest potrzebnych dla danej liczby poziomów.')

def number_of_cans(levels):
    total=0
    for number in range(levels+1):
        total += number
    print('Potrzeba' , total , 'puszek do budowy wieży!!')

number_of_cans (11)