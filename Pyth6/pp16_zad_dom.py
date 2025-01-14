#a

def merge_lists_without_duplicates(source, target):
    for element in source:
        if element not in target:
            target.append(element)

def transform_data(list):
    result = []
    merge_lists_without_duplicates(list, result)
    return tuple(result)

print(transform_data([1,2,3,4,4,3,2,1,1]))

#b

def tow(n):
    if n < 1:
        return 0
    if n < 2:
        return 1

    return n + tow(n-1)

#0 1 2 3 4  5..
#0 1 3 6 10 15..

for n in range(0,10):
    print(n, "->", tow(n))

print()

# lub

def tower(levels):
    total = 0
    for number in range(levels + 1):
        total += number
    print(total)

for n in range(0,11):
    print(n,":"), tower(n)

print()

def levels(cans):
    level=0
    number=[]
    while level+sum(number) < cans:
        level+=1
        number.append(level)
    print(level)

for n in range(0,56):
    print(n,":"), levels(n)

#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15..
#0 1   2     3       4              5..

#c



def define_players():
    players = {}
    players_total = int(input("Podaj liczbę graczy (od 1 do 8): "))
    for i in range(players_total):
        player = define_player(i+1)
        players.update(player) # lub players.update(define_player(i+1)
    return players

def define_player(player_number):
    player_words = []
    player_name = input("Podaj imię {} gracza: ".format(player_number))
    return {player_name: player_words}

#players = define_players()
#print(players)

def is_winner(players):
    i = 0
    for player in players.keys():
        if players[player(i+1)] != players[player(i)]:
           break

def count_words(players, win_words):
    counter = 1
    while True:
        print("\nTura", counter)
        for player in players.keys():
            player_words= int(input("Podaj"+str(counter)+"słowo dla gracza - {}: ".format(player)))
            players[player].append(player_words)
            if is_winner(players, win_words):
                return player
        counter +=1
    return "winner"

def show_results(players, winner):
    print("\nWygrał gracz o imieniu {}, brawo!:".format(winner))
    print()
    print("Szczegółowa tabela wyników")
    for player, words in players.items():
        print(player, "->", words)

players = define_players()
winner = is_winner(players)
#show_results(players, winner)

