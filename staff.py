'''
File: staff.py
Description: Abstract base class for all zoo staff members.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name, employee_id):
        self._name = name
        self._employee_id = employee_id

    @property
    def name(self):
        return self._name

    @property
    def employee_id(self):
        return self._employee_id

    @abstractmethod
    def perform_duty(self):
        pass

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id}) - {self.__class__.__name__}"