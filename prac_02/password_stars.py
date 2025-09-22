"""
MIN_LENGTH = 8
function main():
    get password
    print_stars {password}
function get_password():
    get password
    while len(password) < MIN_LENGTH:
        print "password is too short, please enter a longer password"
        get password
    return password
function print_stars(password, symbol = "*"):
    print "Pythonista + symbol * len(password)"
if __name__ == '__main__':
    main()

"""
MIN_LENGTH = 8
def main():
    password = get_password()
    print_stars(password)
def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print("password is too short, please enter a longer password")
        password = input("Enter your password: ")
    return password
def print_stars(password, symbol = "*"):
    print("Pythonista: " + symbol * len(password))
if __name__ == '__main__':
    main()