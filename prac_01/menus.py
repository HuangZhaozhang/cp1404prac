"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""


def main():
    # Get username
    name = input("Enter your name: ")

    # Core logic of loop
    choice = ''
    while choice != 'Q':
        # Display menu
        print("\nMenu:")
        print("H - Hello")
        print("G - Goodbye")
        print("Q - Quit")

        # Get user choice
        choice = input("Please choose an option: ").upper()

        # Execution of operations
        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        elif choice == 'Q':
            continue  # preparation of quiting loop
        else:
            print("Invalid choice.")

    # Final reminder
    print("Finished.")


if __name__ == "__main__":
    main()