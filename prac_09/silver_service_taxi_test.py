from prac_09.silver_service_taxi import SilverServiceTaxi
def test_silver_service_taxi():
    """Test SilverServiceTaxi functionality"""
    # Test the example from the requirements: Hummer with fanciness 4, 18km trip
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print("Created SilverServiceTaxi:")
    print(hummer)
    print()
    # Start fare and drive 18km
    hummer.start_fare()
    distance_driven = hummer.drive(18)
    print(f"After driving {distance_driven}km:")
    print(hummer)

    # Calculate and display fare
    fare = hummer.get_fare()
    print(f"Total fare: ${fare:.2f}")

    # Verify the calculation matches expected result
    expected_base = 18 * (1.23 * 4)  # 18km * ($1.23 * 4)
    expected_total = expected_base + 4.50  # Plus flagfall
    rounded_expected = round(expected_total * 10) / 10  # Rounded to nearest 10c

    print(f"Expected calculation: 18km * ($1.23 * 4) + $4.50 = ${expected_total:.2f}")
    print(f"Rounded to 10c: ${rounded_expected:.2f}")
    print(f"Actual fare: ${fare:.2f}")
    print(f"Calculation correct: {abs(fare - rounded_expected) < 0.01}")


def test_different_fanciness():
    """Test different fanciness factors"""
    test_cases = [
        ("Standard Luxury", 100, 2.0),
        ("Premium Luxury", 100, 3.5),
        ("Basic Silver", 100, 1.2)
    ]

    for name, fuel, fanciness in test_cases:
        taxi = SilverServiceTaxi(name, fuel, fanciness)
        taxi.start_fare()
        taxi.drive(10)  # Drive 10km
        fare = taxi.get_fare()
        print(f"{name} (fanciness={fanciness}): ${fare:.2f}")


def test_rounding_enhancement():
    """Test that the rounding enhancement works correctly"""
    # Test a case that should demonstrate rounding
    taxi = SilverServiceTaxi("Test Taxi", 100, 1.0)
    taxi.start_fare()
    taxi.drive(7)  # 7km * $1.23 = $8.61 + $4.50 flagfall = $13.11 → should round to $13.10

    fare = taxi.get_fare()
    print(f"7km trip with base price:")
    print(f"Unrounded: 7 * 1.23 + 4.50 = $13.11")
    print(f"Rounded to 10c: ${fare:.2f}")
    print(f"Correctly rounded: {fare == 13.10}")

if __name__ == '__main__':
    test_silver_service_taxi()
    test_different_fanciness()
    test_rounding_enhancement()