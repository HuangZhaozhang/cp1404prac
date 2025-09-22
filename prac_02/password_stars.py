MIN_LENGTH = 8
password = input("Enter your password: ")
while len(password) < MIN_LENGTH:
    print("password is too short, please enter a longer password")
    password = input("Enter your password: ")
print("Pythonista" + "*" * len(password))