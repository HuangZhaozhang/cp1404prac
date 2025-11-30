"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)  # Use join to add space division


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"


    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"


    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these

    # Test default fuel value
    car_default = Car()
    assert car_default.fuel == 0, "Car does not set default fuel correctly"

    # Test passed fuel value
    car_custom = Car(fuel=10)
    assert car_custom.fuel == 10, "Car does not set custom fuel correctly"

    print("All Car tests passed!")


def main():
    """Main function to run all tests."""
    run_tests()

    # (PyCharm may see your >>> doctest comments and run doctests anyway.)
    doctest.testmod(verbose=True)

    print("All tests completed!")


if __name__ == '__main__':
    main()