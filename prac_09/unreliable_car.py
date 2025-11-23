import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A specialized version of Car with reliability-based driving capability"""

    def __init__(self, name="", fuel=0, reliability=0.0):
        """Initialize an UnreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive based on reliability probability

        Args:
            distance: Distance to attempt driving

        Returns:
            int: Actual distance driven (0 if car fails)
        """
        # Generate random number between 0-100
        random_number = random.uniform(0, 100)

        # Drive only if random number is less than reliability threshold
        if random_number < self.reliability:
            # Call parent class drive method
            return super().drive(distance)
        else:
            # Car malfunction - drive 0 km
            return 0

    def __str__(self):
        """Return string representation of unreliable car"""
        return f"{super().__str__()}, reliability={self.reliability}%"