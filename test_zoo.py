'''
File: test_zoo.py
Description: Unit tests for the Zoo Management System.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

import unittest
from zoo import Zoo
from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian


class TestZooManagement(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.zoo = Zoo()
        self.lion = Mammal("Leo", "Lion", 5, "carnivore")
        self.penguin = Mammal("Pingu", "Penguin", 2, "carnivore")
        self.parrot = Bird("Polly", "Parrot", 1, "herbivore")
        self.savannah = Enclosure("Savannah", "Large", "savannah")
        self.arctic = Enclosure("Arctic", "Large", "arctic")

        self.zoo.add_animal(self.lion)
        self.zoo.add_animal(self.penguin)
        self.zoo.add_animal(self.parrot)
        self.zoo.add_enclosure(self.savannah)
        self.zoo.add_enclosure(self.arctic)

    def test_animal_creation(self):
        """Test that animals are created with correct attributes"""
        self.assertEqual(self.lion.name, "Leo")
        self.assertEqual(self.lion.species, "Lion")
        self.assertEqual(self.lion.age, 5)
        self.assertEqual(self.lion.diet, "carnivore")

    def test_enclosure_suitability(self):
        """Test enclosure suitability for different animals"""
        self.assertTrue(self.savannah.is_suitable_for(self.lion))
        self.assertTrue(self.arctic.is_suitable_for(self.penguin))
        self.assertFalse(self.savannah.is_suitable_for(self.parrot))

    def test_animal_assignment(self):
        """Test assigning animals to enclosures"""
        result = self.zoo.assign_animal_to_enclosure(self.lion, self.savannah)
        self.assertIn("Added Leo to Savannah", result)
        self.assertEqual(self.lion.enclosure, self.savannah)
        self.assertIn(self.lion, self.savannah.animals)

    def test_invalid_animal_assignment(self):
        """Test that invalid animal assignments raise errors"""
        with self.assertRaises(ValueError):
            self.zoo.assign_animal_to_enclosure(self.parrot, self.savannah)

    def test_health_system(self):
        """Test health record functionality"""
        record = self.lion.add_health_record("Test injury", "Low", "Rest")
        self.assertEqual(record.animal, self.lion)
        self.assertEqual(record.issue_description, "Test injury")
        self.assertEqual(record.severity, "Low")
        self.assertFalse(record.is_resolved)

    def test_staff_creation(self):
        """Test staff creation and assignment"""
        keeper = Zookeeper("Alice", 1)
        vet = Veterinarian("Bob", 2)

        keeper.assign_to_enclosure(self.savannah)
        vet.assign_to_animal(self.lion)

        self.assertIn(self.savannah, keeper.assigned_enclosures)
        self.assertIn(self.lion, vet.assigned_animals)

    def test_critical_health_movement_restriction(self):
        """Test that animals with critical health issues cannot be moved"""
        self.lion.add_health_record("Serious injury", "High", "Surgery")

        with self.assertRaises(ValueError):
            self.lion.enclosure = self.arctic

    def test_zoo_reports(self):
        """Test report generation"""
        self.zoo.assign_animal_to_enclosure(self.lion, self.savannah)
        self.zoo.assign_animal_to_enclosure(self.penguin, self.arctic)

        animal_report = self.zoo.generate_animal_report()
        health_report = self.zoo.generate_health_report()

        self.assertIn("Leo", animal_report)
        self.assertIn("Pingu", animal_report)
        self.assertIn("Healthy Animals", health_report)

    def test_daily_routines(self):
        """Test daily routine execution"""
        keeper = Zookeeper("Alice", 1)
        keeper.assign_to_enclosure(self.savannah)
        self.zoo.add_staff(keeper)

        self.zoo.assign_animal_to_enclosure(self.lion, self.savannah)
        routines = self.zoo.run_daily_routines()

        self.assertTrue(any("Alice" in routine for routine in routines))


if __name__ == '__main__':
    unittest.main()