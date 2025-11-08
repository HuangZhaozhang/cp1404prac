"""
CP1404/CP5632 Practical - Project Class
Estimated time: 4 hours
Actual time: 5 hours
Start time: 04/11/2025 00:00:00
"""

import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return detailed string representation for debugging."""
        return (f"Project({self.name}, {self.start_date.strftime('%d/%m/%Y')}, "
                f"{self.priority}, {self.cost_estimate}, {self.completion_percentage})")

    def is_complete(self):
        """Determine if project is complete (100% completion)."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Less than method to compare projects by priority for sorting."""
        return self.priority < other.priority

    def start_date_after(self, date):
        """Check if project starts after given date."""
        return self.start_date > date