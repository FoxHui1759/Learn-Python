import random

n = random.randint(1, 10)

game_is_end = False
while not game_is_end:
    player_input = int(input("Guess a number between 1 and 10: "))
    if player_input > n:
        print("Sorry, guess again. Too high.")
    elif player_input < n:
        print("Sorry, guess again. Too low.")
    else:
        print(f"Yay, congrats. You have guessed the number {n} correctly!!")
        game_is_end = True
