"""
MENU = C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit
function main():
    print "MENU"
    get choice
    while choice != "Q":
        if choice == "C":
            get celsius
            get fahrenheit
            print "Result: {fahrenheit:.2f} F"
        else if choice == "F":
            get fahrenheit
            get celsius
            print "Result: {celsius:.2f} C"
        else:
            print "Invalid option"
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
function celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
function fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)
if __name__ == "__main__":
    main()

"""
MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
def celsius_to_fahrenheit(celsius):
#Turn Celsius to Fahrenheit
    return celsius * 9 / 5 + 32
def fahrenheit_to_celsius(fahrenheit):
#Turn Fahrenheit to Celsius
    return 5 / 9 * (fahrenheit - 32)
if __name__ == "__main__":
    main()