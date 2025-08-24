import art
import game_data
import random

# Format account info for display
def format_account(account):
    return f"{account['name']}, {account['description']}, from {account['country']}"
        
def higher_lower():
    # Display game logo
    print(art.logo)

    # Create a copy of the data to avoid modifying the original
    data_pool = game_data.data.copy()
    score = 0

    # Game loop runs while there are enough accounts to compare
    while len(data_pool) > 1:

        # Randomly select two distinct accounts
        option_a = random.choice(data_pool)
        data_pool.remove(option_a)
        option_b = random.choice(data_pool)
        data_pool.remove(option_b)

        # Show comparison
        print(f"Compare A: {format_account(option_a)}")        
        print(f"{art.vs}\n")
        print(f"Compare B: {format_account(option_b)}")

        # Get user's guess
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        # Check invalid input
        if user_guess != "A" and user_guess != "B":
            print("Invalid input!")
            break

        # Check if guess is correct and update score
        if user_guess == "A" and option_a["follower_count"] > option_b["follower_count"]:
            score += 1
            print(f"*** Correct! Currect score: {score} *** \n")
        elif user_guess == "B" and option_b["follower_count"] > option_a["follower_count"]:
            score += 1
            print(f"*** Correct! Currect score: {score} *** \n")
        else:
            print(f"*** Wrong. Final score: {score} ***")
            break

    # Replay option
    again = input("Play again? (y/n)").lower()
    if again == "y":
        higher_lower()
    else: 
        exit()

# Start the game
higher_lower()