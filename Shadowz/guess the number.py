import random

num_guess = int(input("give me a number between 1-100\n"))
random_int = random.randint(0, 101)

if num_guess == random_int:
    Print("wow good job (with sarcasam). ")
elif num_guess > random_int
    print("TOO HIGH BOZO")
elif num_guess < random_int
    print("TOO LOW BOZO")