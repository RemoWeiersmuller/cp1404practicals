"""Silver service Taxi class
Estimate: 60 minutes
Actual:   30 minutes
SilverServiceTaxi class, derived from Taxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Class stores details about fancy taxis."""
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Construct the Class"""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        """Return a string for SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return super().get_fare() + self.flagfall
