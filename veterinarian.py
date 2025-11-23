'''
File: veterinarian.py
Description: Veterinarian subclass implementation for animal healthcare.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff
from datetime import datetime


class Veterinarian(Staff):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)
        self._assigned_animals = []

    @property
    def assigned_animals(self):
        return self._assigned_animals

    def assign_to_animal(self, animal):
        if animal not in self._assigned_animals:
            self._assigned_animals.append(animal)

    def perform_duty(self):
        duties = []
        for animal in self._assigned_animals:
            duties.append(self.conduct_health_check(animal))
        return duties

    def conduct_health_check(self, animal):
        health_status = animal.get_health_summary()
        return f"{self.name} checked {animal.name}: {health_status}"

    def treat_animal(self, animal, issue_description, severity, treatment_plan):
        health_record = animal.add_health_record(issue_description, severity, treatment_plan)
        return f"{self.name} treated {animal.name} for {issue_description}"

    def resolve_health_issue(self, animal, issue_description):
        for record in animal._health_records:
            if record.issue_description == issue_description and not record.is_resolved:
                record.resolve_issue()
                return f"{self.name} resolved {animal.name}'s {issue_description}"
        return f"No active health issue found for {animal.name} with description: {issue_description}"

    def __str__(self):
        return f"{super().__str__()} - Animals: {len(self.assigned_animals)}"