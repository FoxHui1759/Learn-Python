import random


class Player:
    def __init__(self, sign):
        self.sign = sign

    def move():
        pass


class Human_Player(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def get_move(self, game):
        valid = False
        while not valid:
            move = int(input(f"{self.sign}'s turn. Input move (0-8): "))
            if move in range(9) and game.board[move] == " ":
                valid = True
            else:
                print("The input is not valid. Try again")
        return move


class Computer_Player(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def get_move(self, game):
        valid = False
        while not valid:
            move = random.randint(0, 8)
            if game.board[move] == " ":
                valid = True
        return move


class Smart_Computer_Player(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def get_move(self, game):
        if game.empty_square_count() == 9:
            return random.randint(0, 8)
        return self.minimax(game)["position"]

    def minimax(self, state):
        max_player = self.sign
        min_player = "X" if self.sign == "O" else "O"

        if state.has_won:
            return {
                "position": None,
                "score": 1 * (1 + state.empty_square_count())
                if state.winner == max_player
                else -1 * (1 + state.empty_square_count()),
            }
