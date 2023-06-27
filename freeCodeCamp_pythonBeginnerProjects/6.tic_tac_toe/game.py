from player import Human_Player, Computer_Player


class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)]

    def print_board(self):
        for row in [self.board[3 * i : (3 * i + 3)] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_instruction():
        for row in [[str(_) for _ in range(9)][3 * i : (3 * i + 3)] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, move, sign):
        assert self.board(int(move)) == " "
        self.board(int(move)) == sign

    def has_won(self, move, sign):
        row_num = move // 3
        col_num = move % 3
        row = self.board[row_num * 3 : row_num * 3 + 3]
        col = [self.board[col_num + i * 3] for i in range(3)]
        if all([s == sign for s in col]) and all([s == sign for s in row]):
            return True

    def draw(self):
        return " " not in self.board

    def start(self, playerX, playerY):
        self.print_instruction()
        sign = "X"
        while True:
            if sign == "X":
                move = playerX.get_move(self.board)
            else:
                move = playerY.get_move(self.board)
            self.make_move(move, sign)
            print(f"{sign} makes a move to square {move}")
            self.print_board()

            if self.has_won(move, sign):
                print(f"{sign} wins!")
                break
            elif self.draw():
                print("It's a draw!")
                break

            sign = "O" if sign == "X" else "X"


if __name__ == "__main__":
    playerX = Human_Player("X")
    playerY = Computer_Player("O")
    t = TicTacToe()

    t.start(playerX, playerY)
