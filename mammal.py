'''
File: mammal.py
Description: Mammal subclass implementation for the zoo system.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal


class Mammal(Animal):
    def __init__(self, name, species, age, diet, fur_color="unknown", enclosure=None):
        super().__init__(name, species, age, diet, enclosure)
        self._fur_color = fur_color

    @property
    def fur_color(self):
        return self._fur_color

    def make_sound(self):
        return "Growl!"

    def give_birth(self):
        return f"{self.name} is giving birth to live young"

    def __str__(self):
        return f"{super().__str__()} with {self.fur_color} fur"