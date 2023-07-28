import random

num_guess = int(input("give me a number between 1-100.\n"))
random_int = random.randint(0, 101)

if num_guess == random_int:
    print("wow, that was amazing!!!!!!!!!!!!!!!!!!!!!!!!!!!")
elif num_guess > random_int:
    print("to high! guess again")
elif num_guess < random_int:
    print("to low! guess again")
6