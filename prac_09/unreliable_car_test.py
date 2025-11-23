from prac_09.unreliable_car import UnreliableCar

def main():
    """Execute all test functions"""
    test_basic_functionality()
    test_never_works_car()
    test_statistical_reliability()
    test_edge_cases()
    test_multiple_drives()


def test_basic_functionality():
    """Test basic functionality of UnreliableCar class"""
    print("=== Basic Functionality Test ===")

    # Create car with 100% reliability (should always drive successfully)
    perfect_car = UnreliableCar("Perfect Car", 100, 100.0)
    distance_driven = perfect_car.drive(50)
    print(f"{perfect_car}")
    print(f"Attempted 50km, actually drove: {distance_driven}km")
    print()


def test_never_works_car():
    """Test car with 0% reliability (should never drive)"""
    print("=== Zero Reliability Test ===")

    broken_car = UnreliableCar("Broken Car", 100, 0.0)
    distance_driven = broken_car.drive(50)
    print(f"{broken_car}")
    print(f"Attempted 50km, actually drove: {distance_driven}km")
    print()


def test_statistical_reliability():
    """Verify reliability statistics through multiple test runs"""
    print("=== Reliability Statistics Test ===")

    # Create car with 70% reliability for statistical testing
    test_car = UnreliableCar("Test Car", 1000, 70.0)
    successful_drives = 0
    total_attempts = 1000
    test_distance = 1  # Test with 1 km per attempt

    # Perform multiple driving attempts
    for i in range(total_attempts):
        distance_driven = test_car.drive(test_distance)
        if distance_driven > 0:
            successful_drives += 1

    # Calculate and display success rate statistics
    success_rate = (successful_drives / total_attempts) * 100
    expected_rate = 70.0  # Expected success rate

    print(f"Total test attempts: {total_attempts}")
    print(f"Successful drives: {successful_drives}")
    print(f"Actual success rate: {success_rate:.1f}%")
    print(f"Expected success rate: {expected_rate}%")
    print(f"Deviation: {abs(success_rate - expected_rate):.1f}%")
    print()


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    # Test low fuel scenario (car may not drive due to unreliability)
    low_fuel_car = UnreliableCar("Low Fuel Car", 10, 50.0)
    distance_driven = low_fuel_car.drive(100)
    print(f"Low fuel test: {low_fuel_car}")
    print(f"Attempted 100km, actually drove: {distance_driven}km")
    print()


def test_multiple_drives():
    """Test consecutive driving attempts"""
    print("=== Consecutive Driving Test ===")

    car = UnreliableCar("Consecutive Test Car", 200, 80.0)
    attempts = [10, 20, 30, 40]  # Four consecutive driving attempts

    print(f"Initial state: {car}")
    for i, distance in enumerate(attempts, 1):
        driven = car.drive(distance)
        print(f"Attempt {i}: Tried {distance}km, Drove {driven}km, Remaining fuel: {car.fuel}")
    print(f"Final state: {car}")

if __name__ == "__main__":
    main()