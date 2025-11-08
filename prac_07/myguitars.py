from guitar import Guitar


def main():
    """Main program to manage guitar inventory"""
    guitars = load_guitars_from_file('guitars.csv')

    print("All guitars:")
    display_guitars(guitars)

    # Sort guitars by year (oldest to newest)
    guitars.sort()
    print("Guitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Add new guitars from user input
    guitars = add_new_guitars(guitars)

    # Save all guitars back to file
    save_guitars_to_file(guitars, 'guitars.csv')

    print("Final guitar list saved to file:")
    display_guitars(guitars)


def load_guitars_from_file(filename):
    """Load guitars from CSV file and return list of Guitar objects"""
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0]
                    year = int(parts[1])
                    cost = float(parts[2])
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty list.")
    return guitars


def save_guitars_to_file(guitars, filename):
    """Save list of Guitar objects to CSV file"""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}")


def display_guitars(guitars):
    """Display all guitars with vintage indicator"""
    for i, guitar in enumerate(guitars, 1):
        vintage_str = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_str}")


def get_guitar_from_user():
    """Get one guitar from user input, return Guitar object or None if user wants to stop"""
    name = input("Name: ").strip()
    if not name:
        return None

    try:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        return Guitar(name, year, cost)
    except ValueError:
        print("Invalid input. Please enter valid year and cost.")
        return None


def add_new_guitars(existing_guitars):
    """Allow user to add new guitars, return updated list"""
    guitars = existing_guitars.copy()
    print("Add new guitars (enter blank for name to finish):")

    guitar = get_guitar_from_user()
    while guitar is not None:
        guitars.append(guitar)
        print(f"{guitar} added.")
        guitar = get_guitar_from_user()

    return guitars
main()