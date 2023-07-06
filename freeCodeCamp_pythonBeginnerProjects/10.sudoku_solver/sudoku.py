def is_valid(board: list) -> bool:
    for i in range(len(board)):
        if len(board[i]) != len(set(board[i])):
            return False
    for j in range(len(board[0])):
        col_j = list(map(lambda x: x[j], board))
        if len(col_j) != len(set(col_j)):
            return False
    
    return True

def get_first_empty(board: list) -> bool:
    for r in range(len(example_board)):
        for c in range(len(example_board[0])):
            if example_board[r][c] == "-1"
            return (r , c)


def solve_sudoku(board: list) -> None:
    (r, c) = get_first_empty(board)
    


if __name__ == "__main__":
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1],
    ]
    if solve_sudoku(example_board):
        print("It's solvable")
        for i in range(len(example_board)):
            print(example_board[i])
    else:
        print("It's not solvable")
