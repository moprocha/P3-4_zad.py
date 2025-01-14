#a

phones = {
    "Adam": 123123123,
    "Karol": 456456456,
    "Mariola": 789789789,
    "Iza": 159753159
}

while True:
    name = input("Podaj imię: ")
    if name == "":
        break
    if name in phones:
        print("Telefon:", phones[name])
    else:
        print("Nie znaleziono telefonu dla imienia", name)

#b

def merge_lists_without_duplicates(source, target):
    for element in source:
        if element not in target:
            target.append(element)

def transform_data(list1, list2, list3):
    result = []
    merge_lists_without_duplicates(list1, result)
    merge_lists_without_duplicates(list2, result)
    merge_lists_without_duplicates(list3, result)
    return tuple(result)



print(transform_data([1,2],[1,1],[4,4,4]))
print(transform_data([1,2,3],[1,2,3],[4,5,6]))
print(transform_data(["Ala","ma"],["Ala","ma","kota"],["Mysz"]))

#c

# players = {"Tomek": [10, 20, 70], "Agata": [30], [30], [30]}

def define_player(player_number):
    player_points = []
    player_name = input("Podaj imię {} gracza: ".format(player_number))
    return {player_name: player_points}

def define_players():
    players = {}
    players_total = int(input("Podaj liczbę graczy (od 1 do 8): "))
    for i in range(players_total):
        player = define_player(i+1)
        players.update(player) # lub players.update(define_player(i+1)
    return players

#players = define_players()
#print(players)

def define_win_points():
    return int(input("Zdefiniuj liczbę punktów wygranej: "))

def is_winner(players, win_points):
    for player in players.keys():
        if sum(players[player]) >= win_points:
            return True
        return False

def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura", counter)
        for player in players.keys():
            player_points = int(input("Podaj punkty dla gracza - {}".format(player)))
            players[player].append(player_points)
            if is_winner(players, win_points):
                return player
        counter +=1
    return "winner"

def show_results(players, winner):
    print("\nWygrał gracz o imieniu {}, brawo!:".format(winner))
    print()
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)

players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)
#