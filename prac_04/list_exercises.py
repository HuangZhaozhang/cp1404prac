"""
function main():

    numbers = []
    for i in range(5):
        get num
        numbers.append(num)

    print "The first number is {numbers[0]}"
    print "The last number is {numbers[-1]}"
    print "The smallest number is {min(numbers)}"
    print "The largest number is {max(numbers)}"
    print "The average of the numbers is {sum(numbers) / len(numbers)}"

main()
"""
def main():
    # Authorized user list
    authorized_users = ['interpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface']
    # Ask for username
    username = input("Please enter your username: ")
    # Check and output the result
    if username in authorized_users:
        print("Access granted")
    else:
        print("Access denied")


    numbers = []
    for i in range(5):
        num = int(input(f"Number: "))
        numbers.append(num)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()