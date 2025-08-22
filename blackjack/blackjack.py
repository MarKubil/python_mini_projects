import pyfiglet  # For generating stylized ASCII text banners
import random    # For drawing random cards

# Standard deck values for Blackjack (Ace = 11, face cards = 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Calculates the score of a hand, adjusting Aces from 11 to 1 if needed
def calculate_score(cards):
    score = sum(cards)
    ace_count = cards.count(11)

    # Adjust Aces if score is over 21
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

def blackjack():
    while True:
        # Prompt user to start the game
        start = input("Do you want to play a game of Blackjack? (y/n) ")
        if start == "y":
            print(pyfiglet.figlet_format("BLACKJACK"))

            # Initialize hands and score
            your_cards = []
            computer_cards = []
            current_score = 0

            # Draw two random cards for the player
            for _ in range(2):
                draw = random.choice(cards)
                your_cards.append(draw)
                current_score = calculate_score(your_cards)

            # Draw one card for the computer
            computer_card = random.choice(cards)
            computer_cards.append(computer_card)

            # Display player's and computer hand and score
            print(f"Your cards: {your_cards}, current score: {current_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            # Player decision loop
            while True:
                more_cards = input("Type 'y' to get another card, or type 'n' to pass: \n")
                if more_cards == "y":
                    draw = random.choice(cards)
                    your_cards.append(draw)
                    current_score = calculate_score(your_cards)
                    print(f"Your cards: {your_cards}, current score: {current_score}")
                    print(f"Computer's first card: {computer_cards[0]}")

                    # Check for bust
                    if current_score > 21:
                        print(pyfiglet.figlet_format("YOU LOST!"))
                        break
                    
                elif more_cards == "n":
                    computer_score = calculate_score(computer_cards)
                    
                    # Computer draws until it beats player score or busts
                    while computer_score < current_score and computer_score < 21:
                        computer_draw = random.choice(cards)
                        computer_cards.append(computer_draw)
                        computer_score = calculate_score(computer_cards)

                    # Show final hands
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

                    # Determine result
                    if computer_score > 21:
                        print(pyfiglet.figlet_format("YOU WIN!"))
                        break
                    elif computer_score > current_score:
                        print(pyfiglet.figlet_format("YOU LOST!"))
                        break
                    elif computer_score == current_score:
                        print(pyfiglet.figlet_format("IT'S A DRAW!"))
                        break
                    else:
                        print(pyfiglet.figlet_format("YOU WIN!"))
                        break
                    
                else:
                    break  # Exit loop on invalid input

        else:
            print("GoodBye!")
            break
# Start the game
blackjack()

