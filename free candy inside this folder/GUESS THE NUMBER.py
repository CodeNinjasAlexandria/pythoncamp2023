import random 

num_guess = int (input("give me a number between 1-100 or i will put you in my basement with all the other children.\n"))
random_int = random.randint(1, 100)

if num_guess == random_int:
    print("no basement for you today!\n")
elif num_guess > random_int:
    print()