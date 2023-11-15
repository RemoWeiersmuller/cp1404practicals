"""
Estimated:  40 min
Actual:     30 min
Test UnreliableCar class inherits Car.
"""


from unreliable_car import UnreliableCar


my_car = UnreliableCar(name='My Car', fuel=100, reliability=80)

print(my_car.drive(10))

print(my_car)