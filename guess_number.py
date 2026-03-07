import random

number = random.randint(1, 100)
guess = 0
attempts = 0

while guess != number:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Correct! You guessed it in", attempts, "attempts")