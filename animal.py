import unittest

class Animal:
    animals_list = []

    def __init__(self, animal_type, legs):
        self.animal_type = animal_type
        self.legs = legs
        if self.animal_type not in Animal.animals_list:
            Animal.animals_list.append(self.animal_type)

    def display_lists(self):
        return str(self.animals_list)

    def describe_animal(self):
        return f"The {self.animal_type} has {self.legs} legs."
    
    def sort_animals(self):
        Animal.animals_list.sort()
        return str(Animal.animals_list)
    
    def compare_legs(self, other):
        if self.legs > other.legs:
            return f"{self.animal_type} > {other.animal_type}."
        elif self.legs < other.legs:
            return f"{self.animal_type} < {other.animal_type}."
        else:
            return f"{self.animal_type} = {other.animal_type}."

class TestAnimal(unittest.TestCase):
    def setUp(self):
        # Clear the list for each test to prevent test interference
        Animal.animals_list = []
        self.dog = Animal("Dog", 4)
        self.spider = Animal("Spider", 8)
        self.cat = Animal("Cat", 4)  # Add cat here if needed for sort

    def test_display_lists(self):
        self.assertEqual(self.dog.display_lists(), "['Dog', 'Spider', 'Cat']")

    def test_describe_animal(self):
        self.assertEqual(self.dog.describe_animal(), "The Dog has 4 legs.")

    def test_sort_animals(self):
        Animal.animals_list.remove('Spider')  # Assuming Spider not needed for this test
        self.assertEqual(self.dog.sort_animals(), "['Cat', 'Dog']")

    def test_compare_legs(self):
        self.assertEqual(self.dog.compare_legs(self.spider), "Dog < Spider.")

    def test_compare_legs_equal(self):
        another_dog = Animal("Another Dog", 4)
        self.assertEqual(self.dog.compare_legs(another_dog), "Dog = Another Dog.")

if __name__ == '__main__':
    unittest.main()
