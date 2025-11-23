'''
File: enclosure.py
Description: Enclosure class for managing animal habitats.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    VALID_ENVIRONMENTS = ["savannah", "forest", "aquatic", "desert", "arctic", "tropical"]

    ENVIRONMENT_COMPATIBILITY = {
        "savannah": ["Lion", "Zebra", "Elephant", "Giraffe"],
        "forest": ["Monkey", "Bear", "Deer", "Parrot", "Eagle"],
        "aquatic": ["Penguin", "Seal", "Dolphin", "Shark"],
        "desert": ["Camel", "Snake", "Lizard", "Scorpion"],
        "arctic": ["Penguin", "Polar Bear", "Seal", "Arctic Fox"],
        "tropical": ["Monkey", "Parrot", "Snake", "Frog", "Toucan"]
    }

    def __init__(self, name, size, environment_type):
        self._validate_environment(environment_type)

        self._name = name
        self._size = size
        self._environment_type = environment_type
        self._cleanliness_level = 5  # Scale of 1-5 (5 = very clean)
        self._animals = []

    def _validate_environment(self, environment):
        if environment not in self.VALID_ENVIRONMENTS:
            raise ValueError(f"Invalid environment: {environment}. Must be one of {self.VALID_ENVIRONMENTS}")

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def environment_type(self):
        return self._environment_type

    @property
    def cleanliness_level(self):
        return self._cleanliness_level

    @property
    def animals(self):
        return self._animals.copy()

    def is_suitable_for(self, animal):
        """Check if enclosure is suitable for a specific animal based on species"""
        compatible_species = self.ENVIRONMENT_COMPATIBILITY.get(self.environment_type, [])
        return animal.species in compatible_species

    def add_animal(self, animal):
        if not self.is_suitable_for(animal):
            raise ValueError(
                f"Cannot add {animal.species} to {self.environment_type} enclosure. {animal.species} requires a different environment.")

        if animal in self._animals:
            raise ValueError(f"{animal.name} is already in this enclosure")

        # Check if animal has critical health issues
        if animal.has_critical_health_issue():
            raise ValueError(f"Cannot move {animal.name}: Animal has critical health issues requiring treatment")

        self._animals.append(animal)
        animal.enclosure = self
        return f"Added {animal.name} to {self.name}"

    def remove_animal(self, animal):
        if animal not in self._animals:
            raise ValueError(f"{animal.name} is not in this enclosure")

        self._animals.remove(animal)
        animal.enclosure = None
        return f"Removed {animal.name} from {self.name}"

    def get_status(self):
        status = f"Enclosure: {self.name}\n"
        status += f"Type: {self.environment_type}, Size: {self.size}\n"
        status += f"Cleanliness: {self.cleanliness_level}/5\n"
        status += f"Animals: {len(self.animals)}\n"

        for animal in self.animals:
            status += f"  - {animal}\n"

        return status

    def decrease_cleanliness(self, amount=1):
        self._cleanliness_level = max(1, self._cleanliness_level - amount)

    def clean(self):
        self._cleanliness_level = 5
        return f"{self.name} has been cleaned"

    def __str__(self):
        return f"{self.name} ({self.environment_type})"