import pyfiglet  # For generating stylized ASCII text banners
import random    # For drawing random cards

# Standard deck values for Blackjack (Ace = 11, face cards = 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    # Initialize hands and score
    your_cards = []
    computer_cards = []
    current_score = 0

    # Prompt user to start the game
    start = input("Do you want to play a game of Blackjack? (y/n) ")
    if start == "y":
        print(pyfiglet.figlet_format("BLACKJACK"))

        # Draw two random cards for the player
        for _ in range(2):
            draw = random.choice(cards)
            your_cards.append(draw)
            current_score += draw

        # Display player's hand and score
        print(f"Your cards: {your_cards}, current score: {current_score}")

        # Draw one card for the computer
        computer_card = random.choice(cards)
        computer_cards.append(computer_card)
        print(f"Computer's first card: {computer_cards[0]}")

    else:
        exit()

blackjack()
