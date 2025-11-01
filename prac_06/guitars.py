from prac_06.guitar import Guitar
def main():
    guitars = []
    print("My guitars:")
    #Print guitar message
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    #Pre-adding test datas
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    if guitars:
        print("There are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_str = "vintage" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10.2f}{vintage_str}")
if __name__ == "__main__":
    main()