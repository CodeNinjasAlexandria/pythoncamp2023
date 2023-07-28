import random

num_guess = int(input("Give me a number 1 through 10\n"))
random_int = random.randint(0, 11)

if num_guess == random_int: 
    print("Wow. anyone could do that.")
elif num_guess > random_int:
    print("Too much try again")
elif num_guess < random_int:
    print("Too low try again")
elif num_guess == random_int:
    print("Correct!")