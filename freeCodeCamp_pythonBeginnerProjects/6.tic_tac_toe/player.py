import random


class Player:
    def __init__(self, sign):
        self.sign = sign

    def move():
        pass


class Human_Player(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def get_move(self, board):
        valid = False
        while not valid:
            move = input(f"{self.sign}'s turn. Input move (0-8): ")
            if move in list(map(str, range(9))) and board[int(move)] == " ":
                valid = True
            else:
                print("The input is not valid. Try again")
        return move


class Computer_Player(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def get_move(self, board):
        valid = False
        while not valid:
            move = str(random.randint(0, 8))
            if move in list(map(str, range(9))) and board[int(move)] == " ":
                valid = True
        return move
