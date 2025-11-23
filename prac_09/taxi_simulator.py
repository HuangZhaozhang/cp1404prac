from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main taxi simulator program."""

    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")

    running = True
    while running:
        # Show the bill
        print(f"Bill to date: ${total_bill:.2f}")

        # Menu
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            running = False
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            cost = handle_drive(current_taxi)
            total_bill += cost
        else:
            print("Invalid option")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display available taxis and let user choose one."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def handle_drive(current_taxi):
    """Handle the drive operation with proper error checking."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0

    return drive_taxi(current_taxi)


def drive_taxi(taxi):
    """Drive the selected taxi and return the cost."""
    try:
        distance = float(input("Drive how far? "))

        if distance <= 0:
            print("Distance must be positive")
            return 0.0

        # Start new fare
        taxi.start_fare()
        # Drive taxi
        taxi.drive(distance)
        # Calculate fare
        cost = taxi.get_fare()

        print(f"Your {taxi.name} trip cost you ${cost:.2f}")
        return cost

    except ValueError:
        print("Invalid distance")
        return 0.0


def display_taxis(taxis):
    """Display all available taxis with their numbers."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()