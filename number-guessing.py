secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100.")

while True:
    guess = input("Take a guess: ")
    guess = int(guess)
    attempts = attempts + 1

    secret_number = []
    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Well done! You guessed the number.")
