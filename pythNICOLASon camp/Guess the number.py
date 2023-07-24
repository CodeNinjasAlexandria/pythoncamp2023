import random as r

num = r.randint(1, 100)

guess = int(input("Guess the number 1-100: "))

while guess != num:
    if guess < num: print("Too low.")
    else: print("Too high.")
    guess = int(input("Guess the number 1-100: "))\

print("You got it right!")