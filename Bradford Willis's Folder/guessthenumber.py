import random

num_guess = int(input("Give me a number between 1-100.\n"))
random_int = random.randint(1, 100)

if num_guess == random_int:
    print("Wow, That was amazing! ")
elif num_guess > random_int:
    print("Too High!")
elif num_guess < random_int:
    print("Too Low!")