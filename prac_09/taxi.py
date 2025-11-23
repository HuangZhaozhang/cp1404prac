"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car
class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # Class variable for base price

    def __init__(self, name, fuel):
        """Initialise a Taxi instance."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like the Car class but with current fare details."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip, rounded to nearest 10 cents."""
        fare = self.price_per_km * self.current_fare_distance
        # Round to nearest 10 cents (0.1) as required
        rounded_fare = round(fare * 10) / 10
        return rounded_fare

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven