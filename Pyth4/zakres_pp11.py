# 1 - 300 ile liczb podzielnych przez 3 i 7

print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))
print([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0])
print()
# macierze

row = [1, 2]
matrix = [row, row]
print(matrix)

matrix[0][0] = 99
print(matrix)

# zabezpieczenie

row = [1, 2]
matrix = [row[:], row[:]]
print(matrix)

matrix[0][0] = 99
print(matrix)

# lista list

# tworzymy planszę do gry w szachy

chess_row = ["--","--","--","--","--","--","--","--"]
print(chess_row)
chess_row = ["--" for _ in range(8)]
print(chess_row)
print()
chessboard = [chess_row[:] for _ in range(8)]
print(chessboard)
print()
chessboard = [["--" for _ in range(8)] for _ in range(8)]
print(chessboard)
print()
white_pown = "BP"
black_pown = "CP"

chessboard [3][4] = "BP"
chessboard [2][7] = "CP"

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()
#