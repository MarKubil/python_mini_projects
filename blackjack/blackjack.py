import pyfiglet  # For generating stylized ASCII text banners
import random    # For drawing random cards

# Standard deck values for Blackjack (Ace = 11, face cards = 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Calculates the score of a hand, adjusting Aces from 11 to 1 if needed
def calculate_score(cards):
    score = sum(cards)
    ace_count = cards.count(11)

    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1

    return score

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
            current_score = calculate_score(your_cards)

        # Draw one card for the computer
        computer_card = random.choice(cards)
        computer_cards.append(computer_card)

        # Display player's and computer hand and score
        def display_cards():
            print(f"Your cards: {your_cards}, current score: {current_score}")
            print(f"Computer's first card: {computer_cards[0]}")
        display_cards()

        # Player chooses to draw more cards until they pass or bust
        while current_score <= 21:
            more_cards = input("Type 'y' to get another card, anything else to pass: ")
            if more_cards == "y":
                draw = random.choice(cards)
                your_cards.append(draw)
                current_score = calculate_score(your_cards)
                display_cards()
            else:
                break  # Exit loop on any non-'y' input

        # Final result based on score
        if current_score > 21:
            print("You Lost")
        else:
            print("You passed. Final hand:", your_cards, "Score:", current_score)
    else:
        exit()
# Start the game
blackjack()

