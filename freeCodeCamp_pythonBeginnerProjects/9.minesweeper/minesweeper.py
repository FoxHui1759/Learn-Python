import random


class Board:
    def __init__(self, board_size: int, bombs_num: int) -> None:
        self.board_size = board_size
        self.bombs_num = bombs_num
        self.dug = set()

        self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.plant_bombs()
        self.assign_near_bombs()

    def plant_bombs(self):
        bombs_planted = 0
        while bombs_planted < self.bombs_num:
            (r, c) = (
                random.randint(0, self.bombs_num),
                random.randint(0, self.bombs_num),
            )
            if self.board[r][c] == "*":
                continue
            self.board[r][c] = "*"

    def assign_near_bombs(self):
        pass


def player(board_size: int, bombs_num: int) -> None:
    pass
