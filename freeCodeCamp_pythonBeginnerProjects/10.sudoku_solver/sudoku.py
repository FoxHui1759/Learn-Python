def is_valid(board: list, r: int, c: int, num: int) -> bool:
    if num in board[r]:
        return False

    col = list(map(lambda x: x[c], board))
    if num in col:
        return False

    start_row = r // 3 * 3
    start_col = c // 3 * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def get_first_empty(board: list) -> bool:
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == -1:
                return (r, c)
    return (None, None)


# assume it's a valid board at the beginning
def solve_sudoku(board: list) -> bool:
    (r, c) = get_first_empty(board)
    if not r:
        return True
    for num in range(1, 10):
        if is_valid(board, r, c, num):
            board[r][c] = num
            if solve_sudoku(board):
                return True
            board[r][c] = -1
    else:
        return False


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
