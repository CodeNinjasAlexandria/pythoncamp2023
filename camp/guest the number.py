import random

num_guess = int(input("give me a number between 1-100.\n"))
random_int = random.randint(0, 101)

if num_guess == random_int:
    print("WoW,this was amazing(whit sarcasm). ")
elif num_guess < random_int:
    print("too low! Guess again!")