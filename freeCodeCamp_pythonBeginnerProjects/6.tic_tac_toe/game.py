from player import Human_Player, Computer_Player, Smart_Computer_Player


class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[3 * i : (3 * i + 3)] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_instruction():
        for row in [[str(_) for _ in range(9)][3 * i : (3 * i + 3)] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, move, sign):
        assert self.board[move] == " "
        self.board[move] = sign

    def has_won(self, move, sign):
        row_num = move // 3
        col_num = move % 3
        row = self.board[row_num * 3 : row_num * 3 + 3]
        col = [self.board[col_num + i * 3] for i in range(3)]

        if all([s == sign for s in col]) or all([s == sign for s in row]):
            self.winner = sign
            return True
        diagonal1 = [self.board[i] for i in [0, 4, 8]]
        diagonal2 = [self.board[i] for i in [2, 4, 6]]

        if all([s == sign for s in diagonal1]) or all([s == sign for s in diagonal2]):
            self.winner = sign
            return True
        return False

    def draw(self):
        return " " not in self.board

    def empty_square_count(self):
        return self.board.count(" ")

    def start(game, playerX, playerY):
        game.print_instruction()
        sign = "X"
        while True:
            if sign == "X":
                move = playerX.get_move(game)
            else:
                move = playerY.get_move(game)
            game.make_move(move, sign)
            print(f"{sign} makes a move to square {move}")
            game.print_board()

            if game.has_won(move, sign):
                print(f"{sign} wins!")
                break
            elif game.draw():
                print("It's a draw!")
                break

            sign = "O" if sign == "X" else "X"


if __name__ == "__main__":
    playerX = Human_Player("X")
    playerY = Smart_Computer_Player("O")
    t = TicTacToe()

    t.start(playerX, playerY)
