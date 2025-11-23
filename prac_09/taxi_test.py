from prac_09.taxi import Taxi
def main():
    # Create a taxi
    my_taxi = Taxi("Prius 1",100)
    # Drive taxi
    my_taxi.drive(40)
    # Print the detailed information and price
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    # Reset the pricing and then
    my_taxi.start_fare()
    my_taxi.drive(100)
    # Print the detailed information and price
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
if __name__ == "__main__":
    main()