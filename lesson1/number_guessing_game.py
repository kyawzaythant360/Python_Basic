import random

secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

while True:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            if guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
    else:
        print("Please enter a valid number between 1 and 10.")
