# ☕ Coffee Machine Simulator

A Python-based console app that simulates a coffee vending machine. Users can order drinks, insert coins, receive change, and track resources — all in a modular, expandable design.

---

## 🚀 Features

- Ingredient check before processing orders  
- Coin-based payment system with change calculation  
- Resource tracking (water, milk, coffee, profit)  
- Service commands: `report`, `off`  
- Modular functions for easy upgrades

---

## 📋 Menu

| Drink       | Water (ml) | Milk (ml) | Coffee (g) | Cost ($) |
|-------------|------------|-----------|------------|----------|
| Espresso    | 50         | —         | 18         | 1.50     |
| Latte       | 200        | 150       | 24         | 2.50     |
| Cappuccino  | 250        | 100       | 24         | 3.00     |

---

## 🛠 How It Works

1. User selects a drink (`espresso`, `latte`, `cappuccino`)
2. Machine checks if enough ingredients are available
3. User inserts coins (quarters, dimes, nickels, pennies)
4. If payment is sufficient:
   - Drink is made
   - Ingredients are deducted
   - Profit is updated
   - Change is returned (if applicable)

---

## ⚙️ Commands

- `espresso`, `latte`, `cappuccino` — order drinks  
- `report` — view current resources and profit  
- `off` — shut down the machine

---

## 🔧 Future Ideas

- Refill command with password protection  
- Drink history logging  
- Custom drink builder  
- GUI or web interface

---

## 🧠 Author

Built by Marius — pragmatic, efficient, and always scaling up.

