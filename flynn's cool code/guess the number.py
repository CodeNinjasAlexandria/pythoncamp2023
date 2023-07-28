import random

num_guess = int(input("give me a number from 1 to 10\n"))
random_int = random.randint(0, 101)

if num_guess == random_int:
    print("wow, that was amazing(whith sarcasm it was too high)")
elif num_guess > random_int:
    print("too bad (your trash at this)")
elif num_guess < random_int:
    print("too bad (your trash at this it was too low)")