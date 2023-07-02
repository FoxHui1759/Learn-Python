import random


class Board:
    def __init__(self, board_size: int, bombs_num: int) -> None:
        self.board_size = board_size
        self.bombs_num = bombs_num
        self.dug = set()

        self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.plant_bombs()
        self.assign_near_bombs_num()

    def plant_bombs(self) -> None:
        bombs_planted = 0
        while bombs_planted < self.bombs_num:
            (r, c) = (
                random.randint(0, self.bombs_num - 1),
                random.randint(0, self.bombs_num - 1),
            )
            if self.board[r][c] == "*":
                continue
            self.board[r][c] = "*"
            bombs_planted += 1

    def near_bombs_num(self, r: int, c: int) -> int:
        count = 0
        for i in range(max(0, r - 1), min(self.board_size - 1, r + 1) + 1):
            for j in range(max(0, c - 1), min(self.board_size - 1, c + 1) + 1):
                if (i, j) == (r, c):
                    continue
                if self.board[i][j] == "*":
                    count += 1
        return count

    def assign_near_bombs_num(self) -> None:
        for r in range(self.board_size):
            for c in range(self.board_size):
                self.board[r][c] = self.near_bombs_num(r, c)

    def __str__(self) -> str:
        visible_board = [
            [None for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "
        string_rep = ""
        widths = []
        for idx in range(self.board_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.board_size)]
        indices_row = "   "
        cells = []
        for idx, col in enumerate(indices):
            format = "%-" + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += "  ".join(cells)
        indices_row += "  \n"

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx, col in enumerate(row):
                format = "%-" + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += " |".join(cells)
            string_rep += " |\n"

        str_len = int(len(string_rep) / self.board_size)
        string_rep = indices_row + "-" * str_len + "\n" + string_rep + "-" * str_len

        return string_rep


def play(board_size=10, bombs_num=10) -> None:
    board = Board(board_size, bombs_num)
    print(board)


if __name__ == "__main__":
    play()
