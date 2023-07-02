num_board = [list(range((i * 10), (i + 1) * 10)) for i in range(10)]

transported_board = []
for idx in range(len(num_board[0])):
    columns = map(lambda x: x[idx], num_board)
    transported_board.append(list(columns))

print(transported_board)
