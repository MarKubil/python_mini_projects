import pyfiglet
import random

def number_guessing_game():
    # Display game title using ASCII art
    print(pyfiglet.figlet_format("Number Guessing Game"))
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Ask user to choose difficulty level
    dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attemps = 0 # Initialize attempts
    number = random.randint(1, 100) # Random number to guess

    # Set number of attempts based on difficulty
    if dificulty == 'easy':
         attemps = 10
    elif dificulty == 'hard':
        attemps = 5
    print(f"You have {attemps} attempts remaining to guess the number.")

    # Main game loop
    while attemps > 0:
        guess = int(input("Make a guess: "))    # Get user's guess

        if guess == number:
            # Correct guess
            print(f"*** You got it! The answer was {number} ***")
            again = input("Do you wanna play again? (y/n)")
            if again == "y":
                number_guessing_game()  # Restart game
            else: exit()

        # Guess too high
        if guess > number:
            attemps -= 1
            print(f"*** Too High! Attemps left: {attemps}***")
        # Guess too low
        elif guess < number:
            attemps -= 1
            print(f"*** Too Low! Attemps left: {attemps} ***")

    # No attempts left
    if attemps == 0:
            print("*** You've run out of guesses. ***")
            again = input("Do you wanna play again? (y/n)")
            if again == "y":
                number_guessing_game()    

# Start the game
number_guessing_game()