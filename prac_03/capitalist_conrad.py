"""
import random

# Define constants
STARTING_PRICE = 10.00
MIN_INCREASE = 0
MAX_INCREASE = 0.1  # 10%
MIN_DECREASE = 0
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
FILENAME = "capitalist_conrad_output.txt"

# Initialize variables
get price
get number_of_days

# Open file for writing
out_file = open(FILENAME, 'w')

# Print and write the starting price
print f"Starting price: ${price:.2f}"
print f"Starting price: ${price:.2f}", file=out_file

while MIN_PRICE <= price <= MAX_PRICE:
    get number_of_days
    get price_change
    # 50% chance to increase, 50% chance to decrease
    if random.random() < 0.5:
       get price_change
    else:
       get price_change

    get price

    # Print and write the daily price
    print f"On day {number_of_days} price is: ${price:.2f}"
    print f"On day {number_of_days} price is: ${price:.2f}", file=out_file

# Close the file
out_file.close()
"""
import random

# Define constants
STARTING_PRICE = 10.00
MIN_INCREASE = 0
MAX_INCREASE = 0.1  # 10%
MIN_DECREASE = 0
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
FILENAME = "capitalist_conrad_output.txt"

# Initialize variables
price = STARTING_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Print and write the starting price
print(f"Starting price: ${price:.2f}")
print(f"Starting price: ${price:.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0
    # 50% chance to increase, 50% chance to decrease
    if random.random() < 0.5:
        price_change = random.uniform(MIN_INCREASE, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, -MIN_DECREASE)

    price *= (1 + price_change)

    # Print and write the daily price
    print(f"On day {number_of_days} price is: ${price:.2f}")
    print(f"On day {number_of_days} price is: ${price:.2f}", file=out_file)

# Close the file
out_file.close()