'''
File: animal.py
Description: Abstract base class for all animals in the zoo.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from health_record import HealthRecord
from datetime import datetime


class Animal(ABC):
    def __init__(self, name, species, age, diet, enclosure=None):
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet
        self._enclosure = enclosure
        self._health_records = []
        self._last_fed = None

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age

    @property
    def diet(self):
        return self._diet

    @property
    def enclosure(self):
        return self._enclosure

    @enclosure.setter
    def enclosure(self, new_enclosure):
        # Check if animal is healthy enough to be moved
        if self.has_critical_health_issue():
            raise ValueError(f"Cannot move {self.name}: Animal has critical health issues")
        self._enclosure = new_enclosure

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        self._last_fed = datetime.now()
        return f"{self.name} is eating {self.diet} food"

    def sleep(self):
        return f"{self.name} is sleeping"

    def add_health_record(self, description, severity, treatment_plan=""):
        record = HealthRecord(self, description, severity, treatment_plan)
        self._health_records.append(record)
        return record

    def get_health_summary(self):
        active_issues = [r for r in self._health_records if not r.is_resolved]
        if not active_issues:
            return "Healthy"

        critical_issues = [r for r in active_issues if r.severity == "High"]
        if critical_issues:
            return "Critical Health Issues"
        elif len(active_issues) > 0:
            return "Minor Health Issues"
        return "Healthy"

    def has_critical_health_issue(self):
        active_issues = [r for r in self._health_records if not r.is_resolved]
        return any(r.severity == "High" for r in active_issues)

    def __str__(self):
        return f"{self.name} the {self.species} ({self.__class__.__name__})"