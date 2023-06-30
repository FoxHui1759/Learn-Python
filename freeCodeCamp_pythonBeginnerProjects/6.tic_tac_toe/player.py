import random
import math


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
        move = self.minimax(game, self.sign)["position"]
        print(move)
        return move

    def minimax(self, state, current_player):
        # print("This is minimax")
        max_player = self.sign
        opponent = "X" if current_player == "O" else "O"

        # print("This is test1")
        if state.winner:
            return {
                "position": None,
                "score": 1 * (1 + state.empty_square_count())
                if state.winner == opponent
                else -1 * (1 + state.empty_square_count()),
            }
        if state.draw():
            return {"position": None, "score": 0}

        # print("This is test 2")
        if current_player == max_player:
            best_result = {"position": None, "score": -math.inf}
        else:
            best_result = {"position": None, "score": math.inf}

        # print("This is test 3")
        for move in range(9):
            if state.board[move] == " ":
                state.make_move(move, current_player)
                move_result = self.minimax(state, opponent)
                move_result["position"] = move

                state.board[move] == " "
                state.winner = None
                if current_player == max_player:
                    if move_result["score"] > best_result["score"]:
                        best_result = move_result
                else:
                    if move_result["score"] < best_result["score"]:
                        best_result = move_result
        print(best_result)
        return best_result
