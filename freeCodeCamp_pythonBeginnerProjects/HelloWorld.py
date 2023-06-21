board = ["" for _ in range(9)]

board_2d = [board[i * 3 : (i + 1) * 3] for i in range(3)]
print(board_2d)
