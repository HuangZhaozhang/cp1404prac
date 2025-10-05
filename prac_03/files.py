# 1. Write the name to a file
name = input("Please enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# 2. Read the name from the file and print it
with open("name.txt", "r") as file:
    content = file.read()
    print(f"Hi {content}!")

# 3. Write numbers to a file and read the first two to sum them
# First, create the prac directory if it doesn't exist
import os
if not os.path.exists("prac"):
    os.makedirs("prac")
# Write the numbers
with open("prac/numbers.txt", "w") as file:
    file.write("17\n42\n400")
# Read the first two numbers and sum them
with open("prac/numbers.txt", "r") as file:
    first = int(file.readline())
    second = int(file.readline())
    print(f"The sum of the first two numbers: {first + second}")

# 4. Count the total number of lines in the file
with open("prac/numbers.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
    print(f"There are {count} lines in the file")