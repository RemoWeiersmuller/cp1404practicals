"""
languages
Estimate: 30 minutes
Actual:   30 minutes
Store details about a projects in a class.
"""


class Project:
    """Store details about a projects in a class."""

    def __init__(self, name="project", start_date="31/10/2022", priority=1, cost_estimate=0, completion_percentage=0):
        """Construct a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string with details of projects."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return a string for a list given."""
        return str(self)

    def __lt__(self, other):
        """Return if one project is less than another."""
        return self.priority < other.priority

    def __gt__(self, other):
        """Return if one project is greater than another."""
        return self.priority > other.priority

    def __eq__(self, other):
        """Return if one project is equal to another."""
        return self.priority == other.priority

    def is_incomplete(self):
        """Return if a project is complete."""
        return int(self.completion_percentage) < 100
