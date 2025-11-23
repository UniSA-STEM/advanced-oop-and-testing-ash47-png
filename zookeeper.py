'''
File: zookeeper.py
Description: Zookeeper subclass implementation for zoo operations.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff


class Zookeeper(Staff):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)
        self._assigned_enclosures = []

    @property
    def assigned_enclosures(self):
        return self._assigned_enclosures

    def assign_to_enclosure(self, enclosure):
        if enclosure not in self._assigned_enclosures:
            self._assigned_enclosures.append(enclosure)

    def perform_duty(self):
        duties = []
        for enclosure in self._assigned_enclosures:
            duties.append(self.clean_enclosure(enclosure))
            for animal in enclosure.animals:
                duties.append(self.feed_animal(animal))
        return duties

    def feed_animal(self, animal):
        result = animal.eat()
        return f"{self.name} fed {animal.name}: {result}"

    def clean_enclosure(self, enclosure):
        result = enclosure.clean()
        return f"{self.name} cleaned {enclosure.name}: {result}"

    def __str__(self):
        return f"{super().__str__()} - Enclosures: {len(self.assigned_enclosures)}"

