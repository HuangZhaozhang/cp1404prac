from prac_09.musician import Musician


class Band:
    """Band class that contains a collection of musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and empty musicians collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return f"{self.name} ({', '.join(musician_strings)})"

    def __repr__(self):
        """Return a detailed string representation of the Band."""
        return f"Band(name='{self.name}', musicians={self.musicians})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument."""
        if not self.musicians:
            return f"{self.name} has no musicians!"

        play_results = []
        for musician in self.musicians:
            play_results.append(musician.play())

        return "\n".join(play_results)