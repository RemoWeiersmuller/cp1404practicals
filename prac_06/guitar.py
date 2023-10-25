class Guitar:
    CURRENT_YEAR = 2023

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        return str(self)

    def get_age(self):
        age = self.CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50
