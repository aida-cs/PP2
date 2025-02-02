import random

def guess_number():
    name = input("Hello! What is your name?")
    secret = random.randint(1, 20)
    attempts = 0

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    while True:
        guess = int(input("\nTake a guess: "))
        attempts += 1

        if guess < secret:
            print("Your guess is too low.")
        elif guess > secret:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guess_number()