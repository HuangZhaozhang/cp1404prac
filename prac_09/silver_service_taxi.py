from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness multiplier and flagfall"""

    flagfall = 4.50  # Class variable for flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Multiply base price_per_km by fanciness factor
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall"""
        # Get base fare from parent class (which is already rounded to nearest 10c)
        base_fare = super().get_fare()
        total_fare = base_fare + self.flagfall
        return total_fare

    def __str__(self):
        """Return a string representation like parent but with flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"