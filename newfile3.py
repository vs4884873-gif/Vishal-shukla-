import random

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")

number = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("Too low! ⬇️")
    elif guess > number:
        print("Too high! ⬆️")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts!")
        break