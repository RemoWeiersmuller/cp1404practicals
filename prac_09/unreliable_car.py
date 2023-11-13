"""Unreliable_car that inherits from car."""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Defines a class for unreliable car as a subclass of Car. """

    def __init__(self, reliability: float, **kwargs):
        """construct the class."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only if random number is less than reliability."""
        if randint(0, 100) >= self.reliability:
            distance = 0

        distance_driven = super().drive(distance)
        return distance_driven


