"""
Shop Calculator Pseudocode
DISCOUNT_RATE_ONE = 0.0
DISCOUNT_RATE_TWO = 0.9
function main():
// Input validation for number of items (must be non-negative)
num_items = -1
while num_items < 0:
 try:
    get num_items
    if num_items < 0:
     print "Invalid number of items!"
 except ValueError:
    print "Please enter a valid integer!"

total = 0.0
for i from 0 to num_items - 1:
// Input validation for item price (must be non-negative)
price = -1
while price < 0:
 try:
    get price
    if price < 0:
      print "Price cannot be negative!"
 except ValueError:
print "Please enter a valid price!"
total = total + price

// Apply 10% discount if total exceeds $100
if total > 100:
total = total * DISCOUNT_RATE_TWO

// Print total in currency format (2 decimal places)
print f"Total price for {num_items} items is ${total:.2f}"

// Execute main function
main()
"""

DISCOUNT_RATE = 0.9

def main():
    # Input validation: The number of items must be greater than or equal to 0
    num_items = -1
    while num_items < 0:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                print("Invalid number of items!")
        except ValueError:
            print("Please enter a valid integer!")

    total = 0.0
    for i in range(num_items):
        # Input validation
        price = -1
        while price < 0:
            try:
                price = float(input(f"Price of item: "))
                if price < 0:
                    print("Price cannot be negative!")
            except ValueError:
                print("Please enter a valid price!")
        total += price

    # Apply discount
    if total > 100:
        total *= DISCOUNT_RATE

    # Output in the required format
    print(f"Total price for {num_items} items is ${total:.2f}")


if __name__ == "__main__":
    main()