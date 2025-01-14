#a

def safe_int(arg):
    try:
        return int(arg)
    except:
        return None

print(safe_int(1))
print(safe_int(7.2))
print(safe_int("jeden"))
print()

#b

numbers = []
counter = 1

while True:
    if counter > 3:
        break
    try:
        number = float(input("Podaj {} liczbe zmiennoprzecinkowa: ".format(counter)))
        numbers.append(number)
        counter+=1
    except:
        print("Podana wartosc jest niepoprawna, spróbuj ponownie!")

print(numbers)

#c

def fetch_and_validate_int(standard_msg, error_msg = "To nie jest liczba całkowita."):
    while True:
        try:
            return int(input(standard_msg))
        except:
            print(error_msg)


def define_player(player_number):
    player_points = []
    player_name = input("Podaj imię {} gracza: ".format(player_number))
    return {player_name: player_points}

def define_players():
    players = {}
    players_total = fetch_and_validate_int("Podaj liczbę graczy (od 1 do 8): ")
    for i in range(players_total):
        player = define_player(i+1)
        players.update(player) # lub players.update(define_player(i+1)
    return players

#players = define_players()
#print(players)

def define_win_points():
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ")

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
            player_points = fetch_and_validate_int("Podaj punkty dla gracza - {}: ".format(player))
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