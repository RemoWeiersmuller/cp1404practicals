"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = random.uniform(0.1, 0.2)  # 17.5%

MAX_DECREASE = random.uniform(0.1, 0.2)  # 5%

MIN_PRICE = random.randint(0, 10)

MAX_PRICE = random.randint(100, 1000)

INITIAL_PRICE = random.uniform(10, 50)

OUTPUT_FILE = "capitalist_file_random.txt"

number_of_days = 0
price = INITIAL_PRICE
print(f"${price:,.2f}")

out_file = open(OUTPUT_FILE, "w")

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    number_of_days += 1
    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)
print(f"{MAX_INCREASE} max increase", file=out_file)
print(f"{MAX_DECREASE} max decrease", file=out_file)
print(f"{MIN_PRICE} min price", file=out_file)
print(f"{MAX_PRICE} max price", file=out_file)
print(f"{INITIAL_PRICE} initial price", file=out_file)
out_file.close()
