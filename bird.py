'''
File: bird.py
Description: Bird subclass implementation for the zoo system.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal


class Bird(Animal):
    def __init__(self, name, species, age, diet, wingspan=0.0, can_fly=True, enclosure=None):
        super().__init__(name, species, age, diet, enclosure)
        self._wingspan = wingspan
        self._can_fly = can_fly

    @property
    def wingspan(self):
        return self._wingspan

    @property
    def can_fly(self):
        return self._can_fly

    def make_sound(self):
        return "Chirp!"

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying with {self.wingspan}m wingspan"
        return f"{self.name} cannot fly"

    def __str__(self):
        flight_status = "flying" if self.can_fly else "flightless"
        return f"{super().__str__()} ({flight_status} bird)"