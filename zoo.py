'''
File: zoo.py
Description: Main controller class for managing the entire zoo system.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Zoo:
    def __init__(self, name="Simone's Zoo"):
        self._name = name
        self._animals = []
        self._enclosures = []
        self._staff = []

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals.copy()

    @property
    def enclosures(self):
        return self._enclosures.copy()

    @property
    def staff(self):
        return self._staff.copy()

    def add_animal(self, animal):
        if animal in self._animals:
            raise ValueError(f"{animal.name} is already in the zoo")
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal not in self._animals:
            raise ValueError(f"{animal.name} is not in the zoo")

        # Remove from enclosure first
        if animal.enclosure:
            animal.enclosure.remove_animal(animal)

        self._animals.remove(animal)

    def add_enclosure(self, enclosure):
        if enclosure in self._enclosures:
            raise ValueError(f"{enclosure.name} is already in the zoo")
        self._enclosures.append(enclosure)

    def remove_enclosure(self, enclosure):
        if enclosure not in self._enclosures:
            raise ValueError(f"{enclosure.name} is not in the zoo")

        # Remove all animals from enclosure first
        for animal in enclosure.animals[:]:
            enclosure.remove_animal(animal)

        self._enclosures.remove(enclosure)

    def add_staff(self, staff_member):
        if staff_member in self._staff:
            raise ValueError(f"{staff_member.name} is already staff")
        self._staff.append(staff_member)

    def assign_animal_to_enclosure(self, animal, enclosure):
        if animal not in self._animals:
            raise ValueError(f"{animal.name} is not in the zoo")
        if enclosure not in self._enclosures:
            raise ValueError(f"{enclosure.name} is not in the zoo")

        return enclosure.add_animal(animal)

    def get_animals_by_species(self, species):
        return [animal for animal in self._animals if animal.species.lower() == species.lower()]

    def get_enclosures_by_type(self, environment_type):
        return [enc for enc in self._enclosures if enc.environment_type.lower() == environment_type.lower()]

    def generate_animal_report(self):
        report = f"=== ZOO ANIMAL REPORT ===\n"
        report += f"Total Animals: {len(self.animals)}\n\n"

        by_type = {}
        for animal in self.animals:
            animal_type = animal.__class__.__name__
            if animal_type not in by_type:
                by_type[animal_type] = []
            by_type[animal_type].append(animal)

        for animal_type, animals in by_type.items():
            report += f"{animal_type}s: {len(animals)}\n"
            for animal in animals:
                enclosure_name = animal.enclosure.name if animal.enclosure else "No enclosure"
                health_status = animal.get_health_summary()
                report += f"  - {animal.name} ({animal.species}), Age: {animal.age}, Enclosure: {enclosure_name}, Health: {health_status}\n"
            report += "\n"

        return report

    def generate_health_report(self):
        report = f"=== ZOO HEALTH REPORT ===\n"

        healthy_count = 0
        minor_issues = 0
        critical_issues = 0

        for animal in self.animals:
            health_status = animal.get_health_summary()
            if health_status == "Healthy":
                healthy_count += 1
            elif health_status == "Minor Health Issues":
                minor_issues += 1
            elif health_status == "Critical Health Issues":
                critical_issues += 1

        report += f"Healthy Animals: {healthy_count}\n"
        report += f"Animals with Minor Issues: {minor_issues}\n"
        report += f"Animals with Critical Issues: {critical_issues}\n\n"

        # List animals with health issues
        animals_with_issues = [a for a in self.animals if a.get_health_summary() != "Healthy"]
        if animals_with_issues:
            report += "Animals Needing Attention:\n"
            for animal in animals_with_issues:
                health_status = animal.get_health_summary()
                report += f"  - {animal.name}: {health_status}\n"

        return report

    def run_daily_routines(self):
        routines = []
        for staff in self._staff:
            duties = staff.perform_duty()
            routines.extend(duties)

        # Decrease cleanliness over time
        for enclosure in self._enclosures:
            if len(enclosure.animals) > 0:
                enclosure.decrease_cleanliness(1)

        return routines

    def __str__(self):
        return f"{self.name} - Animals: {len(self.animals)}, Enclosures: {len(self.enclosures)}, Staff: {len(self.staff)}"