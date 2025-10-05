"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

#1. When will a ValueError occur?

#A ValueError occurs when the input for the numerator or denominator is not a valid integer (e.g., entering letters, special symbols, or other non-numeric content).

#2. When will a ZeroDivisionError occur?

#A ZeroDivisionError occurs when the denominator is entered as 0 (since division by zero is not allowed in mathematics).

#3. As the codings
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be Zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")