"""Store details about a guitar in a class."""


class Guitar:
    """Store details about a guitar in a class."""
    CURRENT_YEAR = 2023

    def __init__(self, name="", year=0, cost=0):
        """Construct a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string with details of guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return a string for a list given."""
        return str(self)

    def get_age(self):
        """Get the age of a guitar based of a given CURRENT YEAR."""
        age = self.CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if a guitar is vintage or not."""
        return self.get_age() >= 50
