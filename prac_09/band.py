"""
Band class stores details to musicians.
CP-1404
Jason Kennedy and Remo Weiersmuller
"""


class Band:
    def __init__(self, name: str):
        """Construct the class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string of the object."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a new band member."""
        self.musicians.append(musician)

    def play(self):
        """Returns a string of the band's musician(s) playing."""
        return "\n".join(musician.play() for musician in self.musicians)

