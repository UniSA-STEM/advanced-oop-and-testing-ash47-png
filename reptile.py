'''
File: reptile.py
Description: Reptile subclass implementation for the zoo system.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal


class Reptile(Animal):
    def __init__(self, name, species, age, diet, is_venomous=False, enclosure=None):
        super().__init__(name, species, age, diet, enclosure)
        self._is_venomous = is_venomous
        self._body_temperature = 25  # Default temperature

    @property
    def is_venomous(self):
        return self._is_venomous

    @property
    def body_temperature(self):
        return self._body_temperature

    def make_sound(self):
        return "Hiss!"

    def bask(self, temperature):
        self._body_temperature = temperature
        return f"{self.name} is basking at {temperature}°C"

    def __str__(self):
        venom_status = "venomous" if self.is_venomous else "non-venomous"
        return f"{super().__str__()} ({venom_status} reptile)"