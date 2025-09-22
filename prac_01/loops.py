
# Example: Display all odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count from 0 to 100 in increments of 10
print("a. ", end='')
for num in range(0, 101, 10):
    print(num, end=' ')
print()

# b. Count down from 20 to 1
print("b. ", end='')
for num in range(20, 0, -1):
    print(num, end=' ')
print()

# c. Print the number of asterisks specified by the user
number_of_stars = int(input("Number of stars: "))
print("c. ", end='')
for _ in range(number_of_stars):
    print('*', end='')
print()
# d. Print lines of increasing stars
rows = int (input("Number of rows: "))
for i in range(1, rows + 1):
    print('*'*i)