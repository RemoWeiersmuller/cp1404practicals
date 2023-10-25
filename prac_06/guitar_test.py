"""
languages
Estimate: 30 minutes
Actual:    minutes
"""
from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 2000)

print(f"{gibson.name} get_age() - Expected 100. Got {Guitar.get_age(gibson)}")
print(f"{another_guitar.name} get_age() - Expected 9. Got {Guitar.get_age(another_guitar)}")
print(f"{gibson.name} is_vintage() - Expected True. Got {Guitar.is_vintage(gibson)}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {Guitar.is_vintage(another_guitar)}")
