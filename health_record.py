'''
File: health_record.py
Description: Health record system for tracking animal medical issues.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from datetime import datetime


class HealthRecord:
    def __init__(self, animal, issue_description, severity, treatment_plan=""):
        self._animal = animal
        self._issue_description = issue_description
        self._date_reported = datetime.now()
        self._severity = severity  # Low, Medium, High
        self._treatment_plan = treatment_plan
        self._is_resolved = False
        self._date_resolved = None

    @property
    def animal(self):
        return self._animal

    @property
    def issue_description(self):
        return self._issue_description

    @property
    def date_reported(self):
        return self._date_reported

    @property
    def severity(self):
        return self._severity

    @property
    def treatment_plan(self):
        return self._treatment_plan

    @property
    def is_resolved(self):
        return self._is_resolved

    @property
    def date_resolved(self):
        return self._date_resolved

    def update_treatment(self, new_treatment_plan):
        self._treatment_plan = new_treatment_plan

    def resolve_issue(self):
        self._is_resolved = True
        self._date_resolved = datetime.now()

    def __str__(self):
        status = "Resolved" if self.is_resolved else "Active"
        return f"Health Record: {self.issue_description} ({self.severity}) - {status}"