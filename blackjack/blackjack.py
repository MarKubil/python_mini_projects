import pyfiglet  # For generating stylized ASCII text banners

# Standard deck values for Blackjack (Ace = 11, face cards = 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    start = input("Do you want to play a game of Blackjack? (y/n) ")
    if start == "y":
        print(pyfiglet.figlet_format("BLACKJACK"))
    else: exit()



blackjack()