import random
from words import words

live = 6
target = random.choice(words).upper()
target_list = list(target)
current_word = []
used_letter_list = []


def initiate():
    for i in range(len(target_list)):
        current_word.append("_")


def print_list(list):
    for i in range(len(list)):
        print(" " + list[i], end="")
    print("")


def player_guess():
    global live
    while True:
        guess = input("Guess a letter:")
        if guess in used_letter_list:
            print("You have already used that letter. Guess another letter.")
            continue
        if not guess.isalpha():
            print("You input is invaild. Guess another letter.")
            continue
        break
    used_letter_list.append(guess)
    for i in range(len(target_list)):
        if guess == target_list[i]:
            current_word[i] = guess
            break
    else:
        print("Your letter, " + guess + " is not in the word.")
        live -= 1


def play():
    global live
    while True:
        print(
            "You have " + str(live) + " lives left and You have used these letters:",
            end="",
        )
        print_list(used_letter_list)
        print("Current word:", end="")
        print_list(current_word)
        print("")
        player_guess()

        if target_list == current_word:
            print("Yay you guessed the word, " + target + " !!")
            return
        if live == 0:
            print("Sorry, you die. The word was " + target)
            return


initiate()
play()
