'''
File: main.py
Description: Main demonstration script for the Zoo Management System.
Author: Ashley Kamara
Student ID: 110485796
Username: kama021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from zoo import Zoo
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian


def main():
    print("=== ZOO MANAGEMENT SYSTEM DEMONSTRATION ===\n")

    # 1. Initialize the zoo
    my_zoo = Zoo("Zoo")
    print(f"Created: {my_zoo}\n")

    # 2. Create enclosures
    savannah = Enclosure("Savannah Exhibit", "Large", "savannah")
    aviary = Enclosure("Tropical Aviary", "Medium", "forest")
    reptile_house = Enclosure("Reptile House", "Medium", "tropical")
    arctic_zone = Enclosure("Arctic Zone", "Large", "arctic")

    for enclosure in [savannah, aviary, reptile_house, arctic_zone]:
        my_zoo.add_enclosure(enclosure)
        print(f"Added enclosure: {enclosure}")
    print()

    # 3. Create animals
    simba = Mammal("Simba", "Lion", 5, "carnivore", "golden")
    polly = Bird("Polly", "Macaw", 2, "herbivore", 1.2, True)
    slinky = Reptile("Slinky", "Python", 3, "carnivore", False)
    nemo = Mammal("Nemo", "Penguin", 1, "carnivore", "black and white")
    spike = Reptile("Spike", "Komodo Dragon", 8, "carnivore", True)

    animals = [simba, polly, slinky, nemo, spike]
    for animal in animals:
        my_zoo.add_animal(animal)
        print(f"Added animal: {animal}")
    print()

    # 4. Assign animals to appropriate enclosures
    try:
        print(my_zoo.assign_animal_to_enclosure(simba, savannah))
        print(my_zoo.assign_animal_to_enclosure(polly, aviary))
        print(my_zoo.assign_animal_to_enclosure(slinky, reptile_house))
        print(my_zoo.assign_animal_to_enclosure(nemo, arctic_zone))
        print(my_zoo.assign_animal_to_enclosure(spike, reptile_house))
        print()
    except ValueError as e:
        print(f"Error: {e}\n")

    # 5. Create staff
    alice = Zookeeper("Alice", 1)
    bob = Veterinarian("Bob", 2)

    my_zoo.add_staff(alice)
    my_zoo.add_staff(bob)
    print(f"Added staff: {alice}")
    print(f"Added staff: {bob}\n")

    # 6. Assign staff to their duties
    alice.assign_to_enclosure(savannah)
    alice.assign_to_enclosure(aviary)
    alice.assign_to_enclosure(reptile_house)
    alice.assign_to_enclosure(arctic_zone)

    bob.assign_to_animal(simba)
    bob.assign_to_animal(polly)
    bob.assign_to_animal(slinky)
    bob.assign_to_animal(nemo)
    bob.assign_to_animal(spike)

    # 7. Demonstrate animal behaviors
    print("=== ANIMAL BEHAVIORS ===")
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")
        print(f"{animal.eat()}")
        print(f"{animal.sleep()}")

        # Demonstrate unique behaviors
        if isinstance(animal, Mammal):
            print(animal.give_birth())
        elif isinstance(animal, Bird):
            print(animal.fly())
        elif isinstance(animal, Reptile):
            print(animal.bask(30))
        print()

    # 8. Demonstrate health system
    print("=== HEALTH SYSTEM ===")
    # Bob the vet treats some animals
    print(bob.treat_animal(simba, "Minor paw injury", "Low", "Clean and monitor"))
    print(bob.treat_animal(spike, "Serious infection", "High", "Antibiotics and isolation"))
    print()

    # 9. Run daily routines
    print("=== DAILY ROUTINES ===")
    routines = my_zoo.run_daily_routines()
    for routine in routines:
        print(routine)
    print()

    # 10. Generate reports
    print("=== REPORTS ===")
    print(my_zoo.generate_animal_report())
    print(my_zoo.generate_health_report())

    # 11. Demonstrate enclosure status
    print("=== ENCLOSURE STATUS ===")
    for enclosure in my_zoo.enclosures:
        print(enclosure.get_status())

    # 12. Show staff information
    print("=== STAFF INFORMATION ===")
    for staff in my_zoo.staff:
        print(staff)


if __name__ == "__main__":
    main()