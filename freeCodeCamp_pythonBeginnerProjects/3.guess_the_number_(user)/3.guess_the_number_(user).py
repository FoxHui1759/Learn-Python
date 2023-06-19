import random

feedback = ""
max = 1000
min = 1

while feedback != "C":
    guess = random.randint(min, max)
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ")
    if feedback == "H":
        max = guess - 1
    elif feedback == "L":
        min = guess + 1

print(f"Yay! The computer guessed your number, {guess}, correctly!")
