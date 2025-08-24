# Menu dictionary defines drinks, their required ingredients, and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Resources available in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}

# Handles drink selection and resource check
def handle_order(drink_name):
    drink = MENU[drink_name]
    ingredients = drink["ingredients"]

    # Dynamically check each required ingredient
    for item, amount_required in ingredients.items():
        if resources.get(item, 0) < amount_required:
            print(f"Sorry there is not enough {item}")
            return
        
    # Display drink price before payment    
    print(f"Price of {drink_name.upper()} is ${drink['cost']}")
    insert_coin(drink, drink_name)


# Validates coin input and ensures it's an integer
def get_coin_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Handles coin insertion and payment logic
def insert_coin(drink, drink_name):
    print("Please insert coin: ")

    # Collect coin input and calculate total
    quarters = get_coin_input("How many quarters?: ") * 0.25
    dimes = get_coin_input("How many dimes?: ") * 0.10
    nickles = get_coin_input("How many nickles?: ") * 0.05
    pennies = get_coin_input("How many pennies?: ") * 0.01

    total = quarters + dimes + nickles + pennies
    cost = drink["cost"]

    # Check if payment is sufficient
    if total < cost:
        print(f"Sorry price is ${cost} \nYou inserted: ${total} \nNot enough money. Money refunded.")
        return
    elif total > cost:
        change = round(total - cost, 2)
        resources["profit"] += cost
        print(f"Here is ${change} in change")
    else: 
        resources["profit"] += total
    
    # Proceed to make the drink
    make_drink(drink, drink_name)

        
# Simulates drink delivery
def make_drink(drink, drink_name):
    # Deduct ingredients from resources
    for item, amount_required in drink["ingredients"].items():
        resources[item] -= amount_required

    print(f"Here is your {drink_name.upper()}! Enjoy!")

# Main loop for user interaction
def coffee_machine():
    while True:

        # Prompt user for drink selection
        user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Handle valid drink orders
        if user_prompt in MENU:
            handle_order(user_prompt)
            continue
        # Service mode to shut down
        elif user_prompt == "off":
            print("SERVICE MODE")
            exit()

        # Report current resources
        elif user_prompt == "report":
            print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['profit']}")
        # Handle invalid input
        else:
            print("Invalid input please try again!")
            continue


# Start the coffee machine
coffee_machine()

