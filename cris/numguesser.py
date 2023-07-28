import random

num_guess = int(input("Give me a number between 1-100.\n"))
random_int = random.randint(0, 101)

if num_guess == random_int:

    print("wow, that was amazing (with sarcasm).")
elif num_guess > random_int:
    print('too high')
elif num_guess < random_int:
    print('too low')   

