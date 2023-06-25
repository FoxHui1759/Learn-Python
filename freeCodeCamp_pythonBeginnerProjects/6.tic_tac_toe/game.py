from player import Human_Player, Computor_Player


class game:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.end = False

    def print_board(self):
        for row in [self.board[3 * i : (3 * i + 3)] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_num():
        for row in [[str(_) for _ in range(9)][3 * i : (3 * i + 3)] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def start(self):
        self.print_board_num()

        self.print_board()


t = game()
t.start()
