"""Name	Start Date	Priority	Cost Estimate	Completion Percentage"""

import datetime
class Project:
    def __init__(self, name="project", start_date="31/10/2022", priority=1, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def is_incomplete(self):
        return int(self.completion_percentage) < 100